from sqlalchemy.orm import Session
from app.models.activityModel import Activity
from app.schemas.activitySchema import ActivityCreate

def create_activity(db: Session, activity: ActivityCreate):

    new_activity = Activity(
        action=activity.action,
        user_id=activity.user_id,
        project_id=activity.project_id,
        task_id=activity.task_id
    )

    db.add(new_activity)
    db.commit()
    db.refresh(new_activity)

    return new_activity

def get_project_activities(db: Session, project_id: int):

    return db.query(Activity).filter(
        Activity.project_id == project_id
    ).order_by(Activity.created_at.desc()).all()

def get_task_activities(db: Session, task_id: int):

    return db.query(Activity).filter(
        Activity.task_id == task_id
    ).order_by(Activity.created_at.desc()).all()

def get_all_activities(db: Session):
    return db.query(Activity).all()