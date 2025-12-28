from models import ORM_CLS, ORM_OBJ

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from fastapi import HTTPException


async def get_ad_by_id( session: AsyncSession, orm_cls: ORM_CLS, ad_id: int ) -> ORM_OBJ:
    orm_obj = await session.get( orm_cls, ad_id )
    if orm_obj is None:
        raise HTTPException( 404, "Advertisement not found" )
    return orm_obj


# async def search_ad( session: AsyncSession, orm_cls: ORM_CLS, **queryargs):
#     sel = select(orm_cls)
#     query = sel.filter_by(**queryargs)

#     result = await session.execute(query)
#     return result
async def search_ad( session: AsyncSession, orm_cls: ORM_CLS, search: dict | None = None ):
    query = select(orm_cls)

    for key, value in search:

        query = query.filter(
            (orm_cls.title.ilike(f"%{value}%")) | 
            (orm_cls.descr.ilike(f"%{value}%")) | 
            (orm_cls.author.ilike(f"%{value}%"))
        )

    result = await session.execute(query)
    return result.scalars().all()

async def create_ad( session: AsyncSession, ad_item: ORM_OBJ ):
    try:
        session.add( ad_item )
        await session.commit()
        return ad_item
    except IntegrityError:
        raise HTTPException( 409, "Advertisement already exist" )

async def update_ad( session: AsyncSession, orm_cls: ORM_CLS, ad_id: int, updated_item: dict ):
    ad = await session.get( orm_cls, ad_id )
    if not ad:
        raise HTTPException( 404, "Advertisement not found" )

    for key, value in updated_item:
        if value is not None:
            setattr( ad, key, value )
 
    await session.commit()
    return ad



async def delete_ad( session: AsyncSession, orm_cls: ORM_CLS, ad_id: int):
    ad = await session.get( orm_cls, ad_id )
    if not ad:
        raise HTTPException( 404, "Advertisement not found" )
    
    await session.delete(ad)
    await session.commit()
    return {"deleted_id": ad_id}

