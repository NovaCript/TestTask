from pydantic import BaseModel
from pydantic import ConfigDict
from datetime import datetime


class WalkBase(BaseModel):
    apartment_number: str
    pet_name: str
    pet_breed: str
    walk_date: datetime
    walk_time: datetime

class WalkCreate(WalkBase):
    model_config = ConfigDict(use_enum_values=True)


class WalkRead(WalkBase):
    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    is_walked: bool
