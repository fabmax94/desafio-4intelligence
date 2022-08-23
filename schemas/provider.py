from datetime import datetime

from pydantic import BaseModel


class ProviderBase(BaseModel):
    id: str
    name: str
    company: str
    created_at: datetime
    amount_products: int
