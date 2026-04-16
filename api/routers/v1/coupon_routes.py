from fastapi import APIRouter,Depends,Query
from typing import Optional,Annotated
from schemas.v1.request_schemas.coupon_schemas import CouponCreateSchema,CouponUpdateSchema
from ...handlers.coupon_handler import HandleCouponRequest
from infra.primary_db.main import AsyncSession,get_pg_async_session
from hyperlocal_platform.core.enums.timezone_enum import TimeZoneEnum
from hyperlocal_platform.core.models.req_res_models import SuccessResponseTypDict,ErrorResponseTypDict,BaseResponseTypDict

router=APIRouter(
    prefix='/coupons',
    tags=['Coupons Crud']
)


ASYNC_PG_SESSION=Annotated[AsyncSession,Depends(get_pg_async_session)]
SHOP_ID=""

@router.post('')
async def create_coupon(data:CouponCreateSchema,session:ASYNC_PG_SESSION):
    return await HandleCouponRequest(session=session).create(data=data)

@router.put('')
async def update_coupon(data:CouponUpdateSchema,session:ASYNC_PG_SESSION):
    return await HandleCouponRequest(session=session).update(data=data)

@router.delete('/{coupon_id}')
async def delete_coupon(coupon_id:str,session:ASYNC_PG_SESSION):
    return await HandleCouponRequest(session=session).delete(shop_id=SHOP_ID,coupon_id=coupon_id)

@router.get('')
async def get_coupon(session:ASYNC_PG_SESSION,timezone:Optional[TimeZoneEnum]=Query(TimeZoneEnum.Asia_Kolkata)):
    return await HandleCouponRequest(session=session).get(shop_id=SHOP_ID,timezone=timezone)

@router.get('/')
async def getby_id_coupon(session:ASYNC_PG_SESSION):
    ...

@router.get('/search')
async def search_coupon(session:ASYNC_PG_SESSION):
    ...
