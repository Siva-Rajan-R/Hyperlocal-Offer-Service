from ..models.offers_model import Offers
from sqlalchemy import select,update,delete,func,or_,and_
from sqlalchemy.ext.asyncio import AsyncSession
from icecream import ic
from schemas.v1.db_schemas.offer_schemas import OfferCreateDbSchema,OfferUpdateDbSchema
from models.repo_models.base_repo_model import BaseRepoModel
from typing import Optional,List
from hyperlocal_platform.core.decorators.db_session_handler_dec import start_db_transaction
from hyperlocal_platform.core.enums.timezone_enum import TimeZoneEnum


class OffersRepo(BaseRepoModel):
    def __init__(self, session:AsyncSession):
        super().__init__(session)
        self.offer_cols=(
            Offers.id,
            Offers.offline,
            Offers.online,
            Offers.product_id
        )
    @start_db_transaction
    async def create(self,data:OfferCreateDbSchema):
        self.session.add(Offers(**data.model_dump(mode='json')))
        return True
    
    @start_db_transaction
    async def update(self,data:OfferUpdateDbSchema):
        data_toupdate=data.model_dump(mode='json',exclude=['id','shop_id','product_id'],exclude_none=True,exclude_unset=True)
        ic(data_toupdate)
        if not data_toupdate or len(data_toupdate)<1:
            return False
        
        offer_toupdate=update(
            Offers
        ).where(
            Offers.id==data.id,
            Offers.shop_id==data.shop_id,
            Offers.product_id==data.product_id
        ).values(
            **data_toupdate
        ).returning(Offers.id)

        is_updated=(await self.session.execute(offer_toupdate)).scalar_one_or_none()

        return is_updated
    
    @start_db_transaction
    async def delete(self,shop_id:str,offer_id:str):
        offer_todel=delete(
            Offers
        ).where(Offers.id==offer_id,Offers.shop_id==shop_id).returning(Offers.id)

        is_deleted=(await self.session.execute(offer_todel)).scalar_one_or_none()
        return is_deleted

    
    async def get(self,shop_id:str,limit:int,offset:int,query:str,timezone:TimeZoneEnum):
        created_at=func.date(func.timezone(timezone.value,Offers.created_at))
        if offset<=1:
            offset=0
        offset=offset*limit
        search_term=f"%{query}%"
        ic(offset,search_term,limit,shop_id)
        offers_stmt=(
            select(
                *self.offer_cols,
                created_at.label('created_at')
            )
            .where(
                Offers.shop_id==shop_id,
                or_(
                    Offers.product_id.ilike(search_term)
                )
            ).offset(offset=offset).limit(limit=limit)
        )

        offers=(await self.session.execute(offers_stmt)).mappings().all()

        return offers


    
    async def getby_id(self):
        ...
    
    async def search(self, query, limit = 5,):
        ...