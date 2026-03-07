from sqlalchemy.orm import Session

from app.schemas.activitySchema import ActivityCreate
from app.crud.activityCrud import create_activity

def log_activity(
    db: Session,
    action: str,
    user_id: int,
    project_id: int = None,
    task_id: int = None
):

    activity = ActivityCreate(
        action=action,
        user_id=user_id,
        project_id=project_id,
        task_id=task_id
    )

    create_activity(db, activity)