from pydantic import BaseModel
from typing import Optional


class OfferCreateSchema(BaseModel):
    online:str
    offline:str
    shop_id:str
    product_id:str

class OfferUpdateSchema(BaseModel):
    id:str
    shop_id:str
    product_id:str
    online:Optional[str]=None
    offline:Optional[str]=None