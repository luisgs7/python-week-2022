from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import validator 
from statistics import mean
from datetime import datetime


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)

    @validator("image", "flavor", "cost")
    def validate_rantings(cls, v, field):
        if v < 1 or v > 10:
            raise RuntimeError(f"{filed.name} must be between 1 and 10")
        return v

    @validator("rate", always=True)
    def calculate_rate(cls, v, values):
        rate = mean(
            [
                values["flavor"], 
                values["image"],
                values["cost"]
            ]
        )
        return int(rate)

brewdog = Beer(name="Brewdog", style="NEIPA", flavor=6, image=7, cost=8)
