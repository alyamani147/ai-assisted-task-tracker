from datetime import date
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import and_, func, or_, select
from sqlalchemy.orm import Session

from .database import Base, engine, get_db
from .models import Task
from .schemas import TaskCreate, TaskRead, TaskUpdate

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI-Assisted Task Tracker", version="1.0.0")
STATIC_DIR = Path(__file__).resolve().parent.parent / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


def task_to_read(task: Task) -> TaskRead:
    tags = [tag for tag in task.tags.split(",") if tag]
    overdue = bool(task.due_date and task.due_date < date.today() and task.status != "done")
    return TaskRead(
        id=task.id,
        title=task.title,
        description=task.description,
        status=task.status,
        priority=task.priority,
        due_date=task.due_date,
        tags=tags,
        created_at=task.created_at,
        updated_at=task.updated_at,
        overdue=overdue,
    )


@app.get("/", include_in_schema=False)
def index():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.get("/api/tasks", response_model=list[TaskRead])
def list_tasks(
    status: str | None = None,
    priority: str | None = None,
    search: str | None = None,
    tag: str | None = None,
    overdue: bool | None = Query(default=None),
    db: Session = Depends(get_db),
):
    statement = select(Task)
    conditions = []

    if status:
        conditions.append(Task.status == status)
    if priority:
        conditions.append(Task.priority == priority)
    if search:
        pattern = f"%{search.strip().lower()}%"
        conditions.append(
            or_(
                func.lower(Task.title).like(pattern),
                func.lower(Task.description).like(pattern),
            )
        )
    if tag:
        normalized = tag.strip().lower()
        conditions.append(
            or_(
                Task.tags == normalized,
                Task.tags.like(f"{normalized},%"),
                Task.tags.like(f"%,{normalized}"),
                Task.tags.like(f"%,{normalized},%"),
            )
        )
    if overdue is True:
        conditions.append(and_(Task.due_date < date.today(), Task.status != "done"))

    if conditions:
        statement = statement.where(and_(*conditions))

    statement = statement.order_by(Task.created_at.desc())
    return [task_to_read(task) for task in db.scalars(statement).all()]


@app.post("/api/tasks", response_model=TaskRead, status_code=201)
def create_task(payload: TaskCreate, db: Session = Depends(get_db)):
    task = Task(
        title=payload.title,
        description=payload.description,
        status=payload.status,
        priority=payload.priority,
        due_date=payload.due_date,
        tags=",".join(payload.tags),
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task_to_read(task)


@app.patch("/api/tasks/{task_id}", response_model=TaskRead)
def update_task(task_id: int, payload: TaskUpdate, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    changes = payload.model_dump(exclude_unset=True)
    if "tags" in changes:
        changes["tags"] = ",".join(changes["tags"] or [])
    for key, value in changes.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task_to_read(task)


@app.delete("/api/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
