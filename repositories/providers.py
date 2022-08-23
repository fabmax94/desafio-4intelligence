from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import models.provider as models
import schemas.provider as schemas


def get_provider(db: Session, provider_id: str) -> models.Provider:
    return db.query(models.Provider).filter(models.Provider.id == provider_id).first()


def delete_provider(db: Session, provider_id: str) -> bool:
    db_provider = get_provider(db, provider_id)
    if db_provider is None:
        return False
    db.delete(db_provider)
    db.commit()
    return True


def update_provider(db: Session, provider_id: str, provider: schemas.Provider) -> models.Provider:
    db_provider = get_provider(db, provider_id)
    if db_provider is None:
        return None
    db_provider.id = provider.id
    db_provider.name = provider.name
    db_provider.company = provider.company
    db_provider.created_at = provider.created_at
    db_provider.amount_products = provider.amount_products
    db.commit()
    db.refresh(db_provider)
    return db_provider


def create_provider(db: Session, provider: schemas.Provider) -> models.Provider:
    db_provider = models.Provider(
        id=provider.id,
        name=provider.name,
        company=provider.company,
        created_at=provider.created_at,
        amount_products=provider.amount_products
    )
    db.add(db_provider)
    try:
        db.commit()
    except IntegrityError:
        return None
    db.refresh(db_provider)
    return db_provider
