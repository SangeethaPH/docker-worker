from fastapi import FastAPI
from pydantic import BaseModel
import os
import socket

app = FastAPI(title="Docker Worker Demo")


class Task(BaseModel):
    task_name: str


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "worker": socket.gethostname(),
    }


@app.post("/tasks")
def process_task(task: Task):
    return {
        "message": "Task processed successfully",
        "task_name": task.task_name,
        "worker": socket.gethostname(),
        "process_id": os.getpid(),
    }
