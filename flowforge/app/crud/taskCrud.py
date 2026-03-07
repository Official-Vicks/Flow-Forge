from sqlalchemy.orm import Session
from app.models.taskModel import Task
from app.schemas.taskSchema import TaskCreate, TaskUpdate

def create_task(db: Session, task: TaskCreate, creator_id: int):
    new_task = Task(
        title=task.title,
        description=task.description,
        priority=task.priority,
        project_id=task.project_id,
        assigned_to=task.assigned_to,
        created_by=creator_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

def get_tasks(db: Session):
    return db.query(Task).all()

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, task_id: int, updates: TaskUpdate):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return None

    for key, value in updates.model_dump(exclude_unset=True).items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return task

def delete_task(db: Session, task_id: int):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return None

    db.delete(task)
    db.commit()

    return task