from pydantic import BaseModel
from typing import Optional



class CouponCreateSchema(BaseModel):
    code:str
    shop_id:str

class CouponUpdateSchema(BaseModel):
    id:str
    shop_id:str
    code:str