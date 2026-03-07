from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

from app.db.base import Base


class TaskStatus(str, enum.Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"


class PriorityLevel(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(225), nullable=False)
    description = Column(String(225))

    status = Column(Enum(TaskStatus), default=TaskStatus.todo)
    priority = Column(Enum(PriorityLevel), default=PriorityLevel.medium)

    project_id = Column(Integer, ForeignKey("projects.id"))
    created_by = Column(Integer, ForeignKey("users.id"))
    assigned_to = Column(Integer, ForeignKey("users.id"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationships
    project = relationship("Project", back_populates="tasks")

    assignee = relationship("User",foreign_keys=[assigned_to],back_populates="assigned_tasks")
    creator = relationship("User",foreign_keys=[created_by],back_populates="created_tasks")
    activities = relationship("Activity", back_populates="task")