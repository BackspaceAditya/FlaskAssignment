async function completeTask(id) {
  await fetch(`/complete/${id}`, {method: 'POST'});
  location.reload();
}

async function undoTask(id) {
  await fetch(`/undo/${id}`, {method: 'POST'});
  location.reload();
}

async function deleteTask(id) {
  const response = await fetch(`/delete/${id}`, {method: 'POST'});
  if (response.ok) {
    alert('Task deleted');
    location.reload();
  }
}

async function deleteCompleted() {
  const response = await fetch('/delete_completed', {method: 'POST'});
  if (response.ok) {
    alert('Deleted completed tasks');
    location.reload();
  }
}

async function deleteAll() {
  const response = await fetch('/delete_all', {method: 'POST'});
  if (response.ok) {
    alert('Deleted all tasks');
    location.reload();
  }
}
