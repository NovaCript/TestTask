from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Date, Time, Boolean

from core.models.base import Base
from core.models.mixins.int_id_pk import IntIdPkMixin


class Walk(IntIdPkMixin, Base):
    apartment_number: Mapped[str | None] = mapped_column(String(40))
    pet_name: Mapped[str | None] = mapped_column(String(40))
    pet_breed: Mapped[str | None] = mapped_column(String(100))
    walk_date: Mapped[Date | None] = mapped_column(Date)
    walk_time: Mapped[Time | None] = mapped_column(Time)
    is_walked: Mapped[bool | None] = mapped_column(Boolean)

    __table_args__ = (
        UniqueConstraint("apartment_number", "pet_name", "walk_date", "walk_time"),
    )
