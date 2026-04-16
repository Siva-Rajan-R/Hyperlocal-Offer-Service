from sqlalchemy.ext.asyncio import AsyncSession
from icecream import ic
from schemas.v1.request_schemas.coupon_schemas import CouponCreateSchema,CouponUpdateSchema
from infra.primary_db.services.coupons_service import CouponsService
from typing import Optional,List
from hyperlocal_platform.core.enums.timezone_enum import TimeZoneEnum
from hyperlocal_platform.core.models.req_res_models import SuccessResponseTypDict,ErrorResponseTypDict,BaseResponseTypDict
from fastapi.exceptions import HTTPException


class HandleCouponRequest:
    def __init__(self,session:AsyncSession):
        self.session=session
        
    async def create(self,data:CouponCreateSchema):
        res=await CouponsService(session=self.session).create(data=data)
        if res:
            return SuccessResponseTypDict(
                detail=BaseResponseTypDict(
                    msg="Coupon created successfully",
                    status_code=201,
                    success=True
                )
            )
        
        raise HTTPException(
            status_code=400,
            detail=ErrorResponseTypDict(
                status_code=400,
                success=False,
                msg="Error : Creating Coupons",
                description="Invalid data formats for Coupons"
            )
        )
    
    async def update(self,data:CouponUpdateSchema):
        res=await CouponsService(session=self.session).update(data=data)
        if res:
            return SuccessResponseTypDict(
                detail=BaseResponseTypDict(
                    msg="Coupon updated successfully",
                    status_code=200,
                    success=True
                )
            )
        
        raise HTTPException(
            status_code=400,
            detail=ErrorResponseTypDict(
                status_code=400,
                success=False,
                msg="Error : Updating Coupons",
                description="Invalid data formats for Coupons to update"
            )
        )
    
    async def delete(self,shop_id:str,coupon_id:str):
        res=await CouponsService(session=self.session).delete(shop_id=shop_id,coupon_id=coupon_id)
        ic(res)
        if res:
            return SuccessResponseTypDict(
                detail=BaseResponseTypDict(
                    msg="Coupon deleted successfully",
                    status_code=200,
                    success=True
                )
            )
        
        raise HTTPException(
            status_code=400,
            detail=ErrorResponseTypDict(
                status_code=400,
                success=False,
                msg="Error : Creating Deleting",
                description="Invalid data formats for Coupons to deleting"
            )
        )
    
    async def get(self,shop_id:str,timezone:TimeZoneEnum):
        res=await CouponsService(session=self.session).get(timezone=timezone,shop_id=shop_id)
        return SuccessResponseTypDict(
            detail=BaseResponseTypDict(
                msg="Coupon fetched successfully",
                status_code=200,
                success=True
            ),
            data=res
        )
    
    async def getby_id(self,):
        ...
    
    async def search(self, query, limit = 5,):
        ...