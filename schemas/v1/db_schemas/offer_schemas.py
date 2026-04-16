from pydantic import BaseModel
from typing import Optional


class OfferCreateDbSchema(BaseModel):
    id:str
    online:str
    offline:str
    shop_id:str
    product_id:str

class OfferUpdateDbSchema(BaseModel):
    id:str
    shop_id:str
    product_id:str
    online:Optional[str]=None
    offline:Optional[str]=None