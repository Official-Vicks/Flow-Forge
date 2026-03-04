# app/models/taskModel.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.sql import func
import enum

from app.db.base import Base

class taskStatus(str, enum.Enum):
    todo = "Todo"
    in_progress = "in_progress"
    done = "done"

class priority(str, enum.Enum):
    low = "Low"
    medium = "Medium"
    high = "High"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(225), nullable=False)
    description = Column(String(225))

    status = Column(String(100), default=taskStatus.todo)  # todo | in_progress | done
    priority = Column(String(100), default=priority.medium)  # low | medium | high

    project_id = Column(Integer, ForeignKey("projects.id"))
    assignee_id = Column(Integer, ForeignKey("users.id"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationships
    project = relationship("Project", back_populates="tasks")
    assignee = relationship("User", back_populates="tasks")
    activities = relationship("Activity", back_populates="task")