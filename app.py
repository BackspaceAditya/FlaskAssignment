from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)

tasks = []
next_id = 1

@app.route('/')
def index():
    active = [t for t in tasks if t['completed_at'] is None]
    completed = [t for t in tasks if t['completed_at'] is not None]
    return render_template('index.html', active_tasks=active, completed_tasks=completed)

@app.post('/add')
def add():
    global next_id
    description = request.form.get('description', '').strip()
    if description:
        tasks.append({
            'id': next_id,
            'description': description,
            'created_at': datetime.now(),
            'completed_at': None
        })
        next_id += 1
    return redirect('/')

@app.post('/complete/<int:task_id>')
def complete(task_id):
    for task in tasks:
        if task['id'] == task_id and task['completed_at'] is None:
            task['completed_at'] = datetime.now()
            break
    return ('', 204)

@app.post('/undo/<int:task_id>')
def undo(task_id):
    for task in tasks:
        if task['id'] == task_id and task['completed_at'] is not None:
            task['completed_at'] = None
            break
    return ('', 204)

@app.post('/delete/<int:task_id>')
def delete(task_id):
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return ('', 204)

@app.post('/delete_completed')
def delete_completed():
    global tasks
    tasks = [t for t in tasks if t['completed_at'] is None]
    return ('', 204)

@app.post('/delete_all')
def delete_all():
    global tasks
    tasks = []
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
