from sqlalchemy import String,Integer,Float,Column,TIMESTAMP,func
from ..main import BASE


class Offers(BASE):
    __tablename__="offers"
    id=Column(String,primary_key=True)
    offline=Column(String,nullable=True)
    online=Column(String,nullable=True)
    product_id=Column(String,nullable=False)
    shop_id=Column(String,nullable=False)

    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=func.now())