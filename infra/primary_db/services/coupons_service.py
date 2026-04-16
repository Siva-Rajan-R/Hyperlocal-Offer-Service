from ..models.coupons_model import Coupons
from sqlalchemy import select,update,delete
from icecream import ic
from schemas.v1.db_schemas.coupon_schemas import CouponCreateDbSchema,CouponUpdateDbSchema
from schemas.v1.request_schemas.coupon_schemas import CouponCreateSchema,CouponUpdateSchema
from models.service_models.base_service_model import BaseServiceModel
from ..repos.coupons_repo import CouponsRepo
from typing import Optional,List
from hyperlocal_platform.core.enums.timezone_enum import TimeZoneEnum
from hyperlocal_platform.core.utils.uuid_generator import generate_uuid


class CouponsService(BaseServiceModel):
    async def create(self,data:CouponCreateSchema):
        coupon_id:str=generate_uuid()
        data_toadd=CouponCreateDbSchema(**data.model_dump(mode='json'),id=coupon_id)
        return await CouponsRepo(session=self.session).create(data=data_toadd)
    
    async def update(self,data:CouponUpdateSchema):
        data_toadd=CouponUpdateDbSchema(**data.model_dump(mode='json'))
        return await CouponsRepo(session=self.session).update(data=data_toadd)
    
    async def delete(self,shop_id:str,coupon_id:str):
        return await CouponsRepo(session=self.session).delete(coupon_id=coupon_id,shop_id=shop_id)
    
    async def get(self,timezone:TimeZoneEnum,shop_id:str):
        return await CouponsRepo(session=self.session).get(shop_id=shop_id,timezone=timezone)
    
    async def getby_id(self,):
        ...
    
    async def search(self, query, limit = 5,):
        ...