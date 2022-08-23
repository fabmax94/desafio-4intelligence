from sqlalchemy.orm import Session

import models.provider as models
import schemas.provider as schemas


def get_provider(db: Session, provider_id: str):
    return db.query(models.Provider).filter(models.Provider.id == provider_id).first()


def delete_provider(db: Session, provider_id: str):
    db_provider = get_provider(db, provider_id)
    db.delete(db_provider)
    db.commit()


def update_provider(db: Session, provider_id: str, provider: schemas.ProviderBase):
    db_provider = get_provider(db, provider_id)
    db_provider.id = provider.id
    db_provider.name = provider.name
    db_provider.company = provider.company
    db_provider.created_at = provider.created_at
    db_provider.amount_products = provider.amount_products
    db.commit()


def create_provider(db: Session, provider: schemas.ProviderBase):
    db_provider = models.Provider(**provider)
    db.add(db_provider)
    db.commit()
    db.refresh(db_provider)
