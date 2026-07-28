from datetime import date, timedelta


def create_task(client, **overrides):
    payload = {
        "title": "Write tests",
        "description": "Cover the API behavior",
        "status": "todo",
        "priority": "high",
        "due_date": None,
        "tags": ["backend", "pytest"],
    }
    payload.update(overrides)
    return client.post("/api/tasks", json=payload)


def test_create_task_with_due_date_and_tags(client):
    tomorrow = (date.today() + timedelta(days=1)).isoformat()
    response = create_task(client, due_date=tomorrow, tags=[" Backend ", "API"])

    assert response.status_code == 201
    body = response.json()
    assert body["due_date"] == tomorrow
    assert body["tags"] == ["backend", "api"]
    assert body["overdue"] is False


def test_rejects_empty_tag(client):
    response = create_task(client, tags=["backend", "   "])

    assert response.status_code == 422
    assert "Tags must not be empty" in response.text


def test_overdue_filter_returns_only_open_overdue_tasks(client):
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    tomorrow = (date.today() + timedelta(days=1)).isoformat()
    create_task(client, title="Late open", due_date=yesterday, status="todo")
    create_task(client, title="Late done", due_date=yesterday, status="done")
    create_task(client, title="Future", due_date=tomorrow, status="todo")

    response = client.get("/api/tasks", params={"overdue": "true"})

    assert response.status_code == 200
    assert [task["title"] for task in response.json()] == ["Late open"]


def test_update_due_date_and_tags(client):
    task_id = create_task(client).json()["id"]
    new_date = (date.today() + timedelta(days=7)).isoformat()

    response = client.patch(
        f"/api/tasks/{task_id}",
        json={"due_date": new_date, "tags": ["frontend", "review"]},
    )

    assert response.status_code == 200
    assert response.json()["due_date"] == new_date
    assert response.json()["tags"] == ["frontend", "review"]


def test_filter_by_exact_tag_does_not_match_partial_tag(client):
    create_task(client, title="API task", tags=["api"])
    create_task(client, title="Capital task", tags=["capital"])

    response = client.get("/api/tasks", params={"tag": "api"})

    assert response.status_code == 200
    assert [task["title"] for task in response.json()] == ["API task"]


def test_combined_search_priority_and_tag_filters(client):
    create_task(client, title="Urgent backend fix", priority="high", tags=["backend"])
    create_task(client, title="Urgent UI fix", priority="high", tags=["frontend"])
    create_task(client, title="Routine backend work", priority="low", tags=["backend"])

    response = client.get(
        "/api/tasks",
        params={"search": "urgent", "priority": "high", "tag": "backend"},
    )

    assert response.status_code == 200
    assert [task["title"] for task in response.json()] == ["Urgent backend fix"]


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
