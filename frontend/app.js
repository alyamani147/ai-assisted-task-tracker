const state = { tasks: [] };
const board = document.querySelector('#board');
const dialog = document.querySelector('#task-dialog');
const form = document.querySelector('#task-form');
const message = document.querySelector('#message');

const fields = {
  id: document.querySelector('#task-id'), title: document.querySelector('#title'),
  description: document.querySelector('#description'), status: document.querySelector('#status'),
  priority: document.querySelector('#priority'), dueDate: document.querySelector('#due-date'),
  tags: document.querySelector('#tags')
};

function formatDate(value) {
  if (!value) return 'No due date';
  return new Intl.DateTimeFormat(undefined, { dateStyle: 'medium', timeZone: 'UTC' }).format(new Date(`${value}T00:00:00Z`));
}

function render() {
  document.querySelectorAll('.task-list').forEach((list) => { list.innerHTML = ''; });
  for (const status of ['todo', 'in-progress', 'done']) {
    const list = document.querySelector(`[data-status="${status}"]`);
    const tasks = state.tasks.filter((task) => task.status === status);
    if (!tasks.length) list.innerHTML = '<p class="empty">No tasks</p>';
    for (const task of tasks) {
      const card = document.createElement('article');
      card.className = 'card';
      card.dataset.priority = task.priority;
      card.innerHTML = `
        <h3>${escapeHtml(task.title)}</h3>
        <p>${escapeHtml(task.description || 'No description')}</p>
        <div class="tags">${task.tags.map((tag) => `<span class="tag">${escapeHtml(tag)}</span>`).join('')}</div>
        <div class="meta"><span>${task.priority}</span><span class="${task.overdue ? 'overdue' : ''}">${task.overdue ? 'Overdue · ' : ''}${formatDate(task.due_date)}</span></div>`;
      card.addEventListener('click', () => openDialog(task));
      list.appendChild(card);
    }
  }
}

function escapeHtml(value) {
  const node = document.createElement('div');
  node.textContent = value;
  return node.innerHTML;
}

async function loadTasks() {
  const params = new URLSearchParams();
  const search = document.querySelector('#search').value.trim();
  const priority = document.querySelector('#priority-filter').value;
  const tag = document.querySelector('#tag-filter').value.trim();
  if (search) params.set('search', search);
  if (priority) params.set('priority', priority);
  if (tag) params.set('tag', tag);
  if (document.querySelector('#overdue-filter').checked) params.set('overdue', 'true');
  const response = await fetch(`/api/tasks?${params}`);
  state.tasks = await response.json();
  render();
}

function openDialog(task = null) {
  form.reset();
  fields.id.value = task?.id ?? '';
  fields.title.value = task?.title ?? '';
  fields.description.value = task?.description ?? '';
  fields.status.value = task?.status ?? 'todo';
  fields.priority.value = task?.priority ?? 'medium';
  fields.dueDate.value = task?.due_date ?? '';
  fields.tags.value = task?.tags.join(', ') ?? '';
  document.querySelector('#dialog-title').textContent = task ? 'Edit task' : 'Create task';
  document.querySelector('#delete-task').classList.toggle('hidden', !task);
  message.textContent = '';
  dialog.showModal();
}

async function saveTask(event) {
  event.preventDefault();
  const payload = {
    title: fields.title.value,
    description: fields.description.value,
    status: fields.status.value,
    priority: fields.priority.value,
    due_date: fields.dueDate.value || null,
    tags: fields.tags.value.split(',').map((tag) => tag.trim())
  };
  if (!fields.tags.value.trim()) payload.tags = [];
  const id = fields.id.value;
  const response = await fetch(id ? `/api/tasks/${id}` : '/api/tasks', {
    method: id ? 'PATCH' : 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload)
  });
  if (!response.ok) {
    const error = await response.json();
    message.textContent = error.detail?.[0]?.msg || error.detail || 'Unable to save task';
    return;
  }
  dialog.close();
  await loadTasks();
}

async function deleteTask() {
  if (!fields.id.value || !confirm('Delete this task?')) return;
  await fetch(`/api/tasks/${fields.id.value}`, { method: 'DELETE' });
  dialog.close();
  await loadTasks();
}

document.querySelector('#new-task-button').addEventListener('click', () => openDialog());
document.querySelector('#close-dialog').addEventListener('click', () => dialog.close());
document.querySelector('#cancel-dialog').addEventListener('click', () => dialog.close());
document.querySelector('#delete-task').addEventListener('click', deleteTask);
form.addEventListener('submit', saveTask);

for (const selector of ['#search', '#priority-filter', '#tag-filter', '#overdue-filter']) {
  document.querySelector(selector).addEventListener('input', loadTasks);
  document.querySelector(selector).addEventListener('change', loadTasks);
}
document.querySelector('#clear-filters').addEventListener('click', () => {
  document.querySelector('#search').value = '';
  document.querySelector('#priority-filter').value = '';
  document.querySelector('#tag-filter').value = '';
  document.querySelector('#overdue-filter').checked = false;
  loadTasks();
});

loadTasks();
