from datetime import datetime

from pydantic import BaseModel


class Provider(BaseModel):
    id: str
    name: str
    company: str
    created_at: datetime
    amount_products: int

    class Config:
        orm_mode = True
