from datetime import datetime
from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from walk.schemas import (
    WalkRead,
    WalkCreate,
)

from walk import crud as walk_crud
from utils.raise_http_exception import ex

router = APIRouter(
    tags=["Walk"],
)


@router.get("/orders/{date}", response_model=list[WalkRead])
async def get_orders(
    date: str,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    try:
        walk_date = datetime.strptime(date, "%Y-%m-%d").date()
        walks = await walk_crud.get_walks_by_date(
            session=session,
            walk_date=walk_date,
        )
        return walks
    except ValueError:
        raise ex.invalid_date_format()


@router.post("/orders", response_model=WalkRead)
async def create_order(
    walk_create: WalkCreate,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    if walk_create.walk_time.hour < 7:
        raise ex.walk_too_early()

    if walk_create.walk_time.hour > 23 or (
        walk_create.walk_time.hour == 23
    ):
        raise ex.walk_too_late()

    if walk_create.walk_time.minute not in [0, 30]:
        raise ex.walk_duration_too_long()


    new_walk = await walk_crud.create_walk(
        session=session,
        walk_create=walk_create,
    )
    return new_walk
