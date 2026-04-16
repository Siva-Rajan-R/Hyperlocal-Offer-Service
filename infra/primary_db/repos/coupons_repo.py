from ..models.coupons_model import Coupons
from sqlalchemy import select,update,delete,or_,and_,func
from icecream import ic
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.v1.db_schemas.coupon_schemas import CouponCreateDbSchema,CouponUpdateDbSchema
from models.repo_models.base_repo_model import BaseRepoModel
from typing import Optional,List
from core.decorators.error_handler_dec import catch_errors
from hyperlocal_platform.core.decorators.db_session_handler_dec import start_db_transaction
from hyperlocal_platform.core.enums.timezone_enum import TimeZoneEnum


class CouponsRepo(BaseRepoModel):
    def  __init__(self, session:AsyncSession):
        super().__init__(session)
        self.coupons_cols=(
            Coupons.code,
            Coupons.id
        )

    @start_db_transaction
    async def create(self,data:CouponCreateDbSchema):
        self.session.add(Coupons(**data.model_dump(mode='json')))
        return True
    
    @start_db_transaction
    async def update(self,data:CouponUpdateDbSchema):
        data_toupdate=data.model_dump(mode='json')
        if not data_toupdate or len(data_toupdate)<1:
            return False
        
        coupon_toupdate=update(
            Coupons
        ).where(
            Coupons.id==data.id,
            Coupons.shop_id==data.shop_id
        ).values(
            **data_toupdate
        ).returning(Coupons.id)

        is_updated=(await self.session.execute(coupon_toupdate)).scalar_one_or_none()

        return is_updated
    
    @start_db_transaction
    async def delete(self,coupon_id:str,shop_id:str):
        coupon_todel=delete(
            Coupons
        ).where(
            Coupons.id==coupon_id,
            Coupons.shop_id==shop_id
        ).returning(Coupons.id)
        
        is_deleted=(await self.session.execute(coupon_todel)).scalar_one_or_none()
        return is_deleted
    
    async def get(self,shop_id:str,timezone:TimeZoneEnum):
        created_at=func.date(func.timezone(timezone.value,Coupons.created_at))
        coupon_toget=(await self.session.execute(
            select(
                *self.coupons_cols,
                created_at.label('created_at')
            ).where(
                Coupons.shop_id==shop_id
            )
        )).mappings().all()

        return coupon_toget
    
    async def getby_id(self,):
        ...
    
    async def search(self, query, limit = 5,):
        ...