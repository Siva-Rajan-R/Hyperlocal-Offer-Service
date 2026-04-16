from pydantic import BaseModel
from typing import Optional,List


class ReadDbInventoryCreateModel(BaseModel):
    shop_id:str
    product_id:str
    product_name:str
    online:str
    offline:str

class ReadDbInventoryUpdateModel(BaseModel):
    shop_id:str
    product_id:str
    product_name:Optional[str]
    online:Optional[str]
    offline:Optional[str]


class ReadDbInventoryReadModel(ReadDbInventoryCreateModel):
    ...