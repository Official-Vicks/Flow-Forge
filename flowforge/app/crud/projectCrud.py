from sqlalchemy.orm import Session
from app.models.projectModel import Project


def create_project(db: Session, name: str, description: str, created_by: int):
    project = Project(
        name=name,
        description=description,
        created_by=created_by
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project

def get_projects(db: Session, user):
    if user.role == "admin":
        return db.query(Project).all()

    if user.role == "manager":
        return db.query(Project).filter(Project.created_by == user.id).all()

    return []

def get_project_by_id(db: Session, project_id: int, user):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        return None

    if user.role == "admin":
        return project

    if user.role == "manager" and project.created_by == user.id:
        return project

    return None

def update_project(db: Session, project, update_data: dict):
    for key, value in update_data.items():
        setattr(project, key, value)

    db.commit()
    db.refresh(project)
    return project

def delete_project(db: Session, project):
    db.delete(project)
    db.commit()

