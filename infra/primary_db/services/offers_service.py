from ..models.offers_model import Offers
from sqlalchemy import select,update,delete
from icecream import ic
from schemas.v1.db_schemas.offer_schemas import OfferCreateDbSchema,OfferUpdateDbSchema
from schemas.v1.request_schemas.offer_schemas import OfferCreateSchema,OfferUpdateSchema
from models.service_models.base_service_model import BaseServiceModel
from ..repos.offers_repo import OffersRepo
from typing import Optional,List
from hyperlocal_platform.core.enums.timezone_enum import TimeZoneEnum
from hyperlocal_platform.core.utils.uuid_generator import generate_uuid


class OffersService(BaseServiceModel):
    async def create(self,data:OfferCreateSchema):
        offer_id:str=generate_uuid()
        data_toadd=OfferCreateDbSchema(**data.model_dump(mode='json'),id=offer_id)
        return await OffersRepo(session=self.session).create(data=data_toadd)
    
    async def update(self,data:OfferUpdateSchema):
        data_toupdated=OfferUpdateDbSchema(**data.model_dump(mode='json'))
        return await OffersRepo(session=self.session).update(data=data_toupdated)
    
    async def delete(self,shop_id:str,offer_id:str):
        return await OffersRepo(session=self.session).delete(shop_id=shop_id,offer_id=offer_id)
    
    async def get(self,shop_id:str,offset:int,limit:int,query:str,timezone:TimeZoneEnum):
        return await OffersRepo(session=self.session).get(shop_id=shop_id,limit=limit,offset=offset,query=query,timezone=timezone)
    
    async def getby_id(self):
        ...
    
    async def search(self):
        ...