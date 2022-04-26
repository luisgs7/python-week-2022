from sqlmodel import create_engine

from beerlog import models
from beerlog.config import settings

engine = create_engine(settings.database.url, echo=False)
models.SQLModel.metadata.create_all(engine)