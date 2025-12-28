from fastapi import FastAPI, Query
from typing import Union

from lifespan import lifespan
from dependency import SessionDependency

from schema import AdCreate, AdResponse, AdUpdate
from models import AdsBase



import crud

app = FastAPI(
    title="FastAPI_Homework_1",
    description="Part 1 of FastAPI homework",
    lifespan=lifespan
)

@app.post('/advertisement', response_model=AdResponse)
async def create_adv( session: SessionDependency, ad_item: AdCreate ):
    ad = AdsBase(
        title = ad_item.title,
        descr = ad_item.descr,
        price = ad_item.price,
        author = ad_item.author,
    )
    resp_ad = await crud.create_ad( session, ad)
    return resp_ad

@app.get('/advertisement/{ad_id}', response_model=AdResponse)
async def get_ad( session: SessionDependency, ad_id: int ):
    ad = await crud.get_ad_by_id( session, AdsBase, ad_id )
    return ad


@app.get('/advertisement/')
async def search_adv( session: SessionDependency, 
                    title:  Union[str, None] = None,
                    description:  Union[str, None] = None,
                    price:  Union[int, None] = None,
                    author: Union[str, None] = None ):
    queryargs = {}
    if title:
        queryargs["title"] = title
    if description:
        queryargs["descr"] = description
    if price:
        queryargs["price"] = price
    if author:
        queryargs["author"] = author

    ad = await crud.search_ad( session, AdsBase, queryargs )
    return queryargs

@app.patch('/advertisement/{ad_id}', response_model=AdResponse)
async def get_ad( session: SessionDependency, ad_id: int, update_item: AdUpdate):
    ad = await crud.update_ad( session, AdsBase, ad_id, update_item )
    return ad

@app.delete('/advertisement/{ad_id}')
async def get_ad( session: SessionDependency, ad_id: int ):
    msg = await crud.delete_ad( session, AdsBase, ad_id )
    return msg
