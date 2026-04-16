from fastapi import APIRouter,Depends,Query
from typing import Optional,Annotated
from schemas.v1.request_schemas.offer_schemas import OfferCreateSchema,OfferUpdateSchema
from ...handlers.offer_handler import HandleOfferRequest
from infra.primary_db.main import AsyncSession,get_pg_async_session
from hyperlocal_platform.core.enums.timezone_enum import TimeZoneEnum
from hyperlocal_platform.core.models.req_res_models import SuccessResponseTypDict,ErrorResponseTypDict,BaseResponseTypDict


router=APIRouter(
    prefix='/offers',
    tags=['Offers Crud']
)


ASYNC_PG_SESSION=Annotated[AsyncSession,Depends(get_pg_async_session)]
SHOP_ID="ce3da5ea-97ad-5a18-ac4f-585aa02383e2"

@router.post('')
async def create_offer(data:OfferCreateSchema,session:ASYNC_PG_SESSION):
    return await HandleOfferRequest(session=session).create(data=data)

@router.put('')
async def update_offer(data:OfferUpdateSchema,session:ASYNC_PG_SESSION):
    return await HandleOfferRequest(session=session).update(data=data)

@router.delete('/{offer_id}')
async def delete_offer(offer_id:str,session:ASYNC_PG_SESSION):
    return await HandleOfferRequest(session=session).delete(shop_id=SHOP_ID,offer_id=offer_id)

@router.get('')
async def get_offer(session:ASYNC_PG_SESSION,limit:Optional[int]=Query(10),offset:int=Query(...),q:Optional[str]=Query(''),timezone:Optional[TimeZoneEnum]=Query(TimeZoneEnum.Asia_Kolkata)):
    return await HandleOfferRequest(session=session).get(offset=offset,limit=limit,query=q,timezone=timezone,shop_id=SHOP_ID)

# @router.get('/')
# async def getby_id_offer(session:ASYNC_PG_SESSION):
#     ...

# @router.get('/search')
# async def search_offer(session:ASYNC_PG_SESSION):
#     ...
