from app.db.session import engine
from app.db.base import Base

# Import all models here so they are registered properly
from app.models import userModel, activityModel, projectModel, taskModel  # noqa


def init_db():
    Base.metadata.create_all(bind=engine)