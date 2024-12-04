from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Define a Task model
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
    
print("Hello todo list")

# In-memory database to store tasks
tasks_db: List[Task] = []

# Create a new task
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    tasks_db.append(task)
    return task

# Read all tasks
@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    return tasks_db

# Read a specific task by ID
@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Update a task
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

# Delete a task
@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            deleted_task = tasks_db.pop(index)
            return deleted_task
    raise HTTPException(status_code=404, detail="Task not found")
