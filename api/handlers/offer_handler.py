from sqlalchemy.ext.asyncio import AsyncSession
from icecream import ic
from schemas.v1.request_schemas.offer_schemas import OfferCreateSchema,OfferUpdateSchema
from infra.primary_db.services.offers_service import OffersService
from typing import Optional,List
from hyperlocal_platform.core.enums.timezone_enum import TimeZoneEnum
from hyperlocal_platform.core.models.req_res_models import SuccessResponseTypDict,ErrorResponseTypDict,BaseResponseTypDict
from fastapi.exceptions import HTTPException


class HandleOfferRequest:
    def __init__(self,session:AsyncSession):
        self.session=session
        
    async def create(self,data:OfferCreateSchema):
        res=await OffersService(session=self.session).create(data=data)
        if res:
            return SuccessResponseTypDict(
                detail=BaseResponseTypDict(
                    msg="Offer created successfully",
                    status_code=201,
                    success=True
                )
            )

        raise HTTPException(
            status_code=400,
            detail=ErrorResponseTypDict(
                status_code=400,
                success=False,
                msg="Error : Creating offer",
                description="Invalid data formats for Offers"
            )
        )
    async def update(self,data:OfferUpdateSchema):
        res=await OffersService(session=self.session).update(data=data)
        if res:
            return SuccessResponseTypDict(
                detail=BaseResponseTypDict(
                    msg="Offer updated successfully",
                    status_code=200,
                    success=True
                )
            )
        
        raise HTTPException(
            status_code=400,
            detail=ErrorResponseTypDict(
                status_code=400,
                success=False,
                msg="Error : Updating offer",
                description="Invalid data formats for Offers to update"
            )
        )
    
    
    async def delete(self,shop_id:str,offer_id:str):
        res=await OffersService(session=self.session).delete(shop_id=shop_id,offer_id=offer_id)
        if res:
            return SuccessResponseTypDict(
                detail=BaseResponseTypDict(
                    msg="Offer deleted successfully",
                    status_code=200,
                    success=True
                )
            )
        
        raise HTTPException(
            status_code=400,
            detail=ErrorResponseTypDict(
                status_code=400,
                success=False,
                msg="Error : Deleting offer",
                description="Invalid data formats for Offers to delete"
            )
        )
    

    async def get(self,offset:int,limit:int,query:str,timezone:TimeZoneEnum,shop_id:str):
        res=await OffersService(session=self.session).get(shop_id=shop_id,offset=offset,limit=limit,query=query,timezone=timezone)
        return SuccessResponseTypDict(
            detail=BaseResponseTypDict(
                msg="Offer fetched successfully",
                status_code=200,
                success=True
            ),
            data=res
        )
    
    async def getby_id(self):
        ...
    
    async def search(self):
        ...