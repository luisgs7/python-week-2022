from sqlmodel import SQLModel, Field
from typing import Optional


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int

brewdog = Beer(name="Brewdog", style="NEIPA", flavor=6, image=7, cost=8)
