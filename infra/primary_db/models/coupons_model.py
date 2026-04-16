from sqlalchemy import String,Integer,Float,Column,TIMESTAMP,func
from ..main import BASE


class Coupons(BASE):
    __tablename__="coupons"
    id=Column(String,primary_key=True)
    code=Column(String,nullable=False)
    shop_id=Column(String,nullable=False)

    created_at=Column(TIMESTAMP(timezone=True),server_default=func.now())