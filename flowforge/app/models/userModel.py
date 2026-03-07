from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum

from app.db.base import Base


class UserRole(str, enum.Enum):
    admin = "admin"
    manager = "manager"
    staff = "staff"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    email = Column(String(255), unique=True, index=True, nullable=False)

    hashed_password = Column(String, nullable=False)

    role = Column(Enum(UserRole), nullable=False, default=UserRole.staff)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    # Relationships
    assigned_tasks = relationship("Task",foreign_keys="Task.assigned_to",back_populates="assignee")
    created_tasks = relationship("Task",foreign_keys="Task.created_by",back_populates="creator")
    activities = relationship("Activity", back_populates="user")
    projects = relationship("Project", foreign_keys="Project.created_by",back_populates="owner")