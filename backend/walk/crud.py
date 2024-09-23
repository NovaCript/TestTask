from datetime import datetime
from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from walk.models import Walk
from walk.schemas import WalkCreate


async def get_walks_by_date(
    session: AsyncSession,
    walk_date: datetime,
) -> Sequence[Walk]:
    stmt = select(Walk).where(Walk.walk_date == walk_date)
    stmt = stmt.where(Walk.is_walked == False)
    result = await session.scalars(stmt)
    return result.all()


async def create_walk(
    session: AsyncSession,
    walk_create: WalkCreate,
) -> Walk:
    new_walk = Walk(**walk_create.model_dump())
    session.add(new_walk)
    await session.commit()
    await session.refresh(new_walk)
    return new_walk
