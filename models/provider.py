from sqlalchemy import Column, Integer, String, DateTime

from models import Base


class Provider(Base):
    __tablename__ = "providers"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    company = Column(String)
    created_at = Column(DateTime)
    amount_products = Column(Integer)
