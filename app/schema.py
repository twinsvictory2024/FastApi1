from pydantic import BaseModel
import datetime


class AdCreate( BaseModel ):
    title: str
    descr: str
    price: int
    author: str


class AdResponse( BaseModel ):
    id: int
    created_at: datetime.datetime
    title: str
    descr: str
    price: int
    author: str


class AdUpdate( BaseModel ):
    title: str | None = None
    descr: str | None = None
    price: int | None = None