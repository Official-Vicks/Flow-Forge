from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# ----------------------------
# Base schema
# ----------------------------
class ActivityBase(BaseModel):
    action: str

class ActivityCreate(ActivityBase):
    user_id: int
    project_id: Optional[int] = None
    task_id: Optional[int] = None

class ActivityResponse(ActivityBase):

    id: int
    user_id: int
    project_id: Optional[int]
    task_id: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True