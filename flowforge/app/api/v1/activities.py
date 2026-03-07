from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, require_role, require_manager_or_admin
from app.crud import activityCrud

router = APIRouter()
@router.get("/projects/{project_id}")
def get_project_activity(
    project_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_role)
):

    return activityCrud.get_project_activities(db, project_id)

@router.get("/tasks/{task_id}")
def get_task_activity(
    task_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_role)
):

    return activityCrud.get_task_activities(db, task_id)

@router.get("/activity-log")
def get_all_activities(
    db: Session = Depends(get_db),
    current_user = Depends(require_manager_or_admin)
):

    return activityCrud.get_all_activities(db)