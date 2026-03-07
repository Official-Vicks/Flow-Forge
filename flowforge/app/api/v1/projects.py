from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.schemas.projectSchema import ProjectCreate, ProjectUpdate, ProjectResponse
from app.crud import projectCrud
from app.core.dependencies import require_admin, require_manager_or_admin, require_role
from typing import List
from app.services.activity_logger import log_activity


router = APIRouter()

@router.post("/create", response_model=ProjectResponse)
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_manager_or_admin)
):
    
    
    new_project =  projectCrud.create_project(
        db=db,
        name=project.name,
        description=project.description,
        created_by=current_user.id
    )
    log_activity(
        db=db,
        action= f"User: {current_user.full_name} created project: {new_project.name}",
        project_id= new_project.id,
        user_id=current_user.id
    )

    return new_project

@router.get("/projects", response_model=List[ProjectResponse])
def get_projects(
    db: Session = Depends(get_db),
    current_user = Depends(require_manager_or_admin)
):
    return projectCrud.get_projects(db, current_user)

@router.get("/get_project{project_id}", response_model=ProjectResponse)
def get_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_manager_or_admin)
):
    project = projectCrud.get_project_by_id(db, project_id, current_user)

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Project not found or access denied"
        )

    return project

@router.put("/update{project_id}", response_model=ProjectResponse)
def update_project(
    project_id: int,
    project_update: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(require_manager_or_admin)
):
    project = projectCrud.get_project_by_id(db, project_id, current_user)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found or access denied")

    if project.created_by != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed to update")

    updated_project = projectCrud.update_project(
        db,
        project,
        project_update.model_dump(exclude_unset=True)
    )

    log_activity(
        db=db,
        action= f"User: {current_user.full_name} updated Project to: {updated_project.name}",
        user_id= current_user.id,
        project_id=updated_project.id
    )
    return updated_project

@router.delete("/delete{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_manager_or_admin)
):
    project = projectCrud.get_project_by_id(db, project_id, current_user)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if project.created_by != current_user.id:
        raise HTTPException(status_code=403, detail="Not allowed to delete")

    log_activity(
        db=db,
        action= f"User: {current_user.full_name} deleted project: {project.name}",
        user_id= current_user.id,
        project_id=project_id
    )
    projectCrud.delete_project(db, project)

    return {"detail": "Project deleted successfully"}