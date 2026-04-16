from pydantic import BaseModel
from typing import Optional



class CouponCreateDbSchema(BaseModel):
    id:str
    code:str
    shop_id:str

class CouponUpdateDbSchema(BaseModel):
    id:str
    shop_id:str
    code:str