from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.taskSchema import TaskCreate, TaskUpdate, TaskResponse
from app.crud import taskCrud
from app.core.dependencies import get_db, require_admin, require_manager_or_admin, require_role
from typing import List
from app.services.activity_logger import log_activity

router = APIRouter()

@router.post("/create", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_manager_or_admin)
):
    
    new_task = taskCrud.create_task(db, task, current_user.id)
    log_activity(
        db=db,
        action= f"User: {current_user.full_name} created task: {new_task.title}",
        user_id=current_user.id,
        task_id=new_task.id
    )
    return new_task

@router.get("/tasks", response_model=List[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db),
    current_user = Depends(require_manager_or_admin)
):

    return taskCrud.get_tasks(db)

@router.get("/get_task{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_manager_or_admin)
):

    task = taskCrud.get_task(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task

@router.patch("/update{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    updates: TaskUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(require_role)
):

    task = taskCrud.update_task(db, task_id, updates)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    log_activity(
        db=db,
        action= f"User: {current_user.full_name} updated Task to: {task.title}",
        user_id= current_user.id,
        task_id=task_id
    )
    return task

@router.delete("/delete{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_manager_or_admin)
):

    task = taskCrud.delete_task(db, task_id)

    log_activity(
        db=db,
        action= f"User: {current_user.full_name} deleted task: {task.title}",
        user_id=current_user.id
    )
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted"}