from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import schemas.provider
from models import Base, engine, SessionLocal
from repositories.providers import create_provider, get_provider, delete_provider, update_provider


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/providers/", response_model=schemas.provider.Provider)
def create_provider_api(provider: schemas.provider.Provider, db: Session = Depends(get_db)):
    db_provider = create_provider(db=db, provider=provider)
    if db_provider is None:
        raise HTTPException(status_code=404, detail="This Provider already exist")
    return db_provider


@app.put("/providers/{provider_id}", response_model=schemas.provider.Provider)
def update_provider_api(provider_id: str, provider: schemas.provider.Provider, db: Session = Depends(get_db)):
    db_provider = update_provider(db=db, provider_id=provider_id, provider=provider)
    if db_provider is None:
        raise HTTPException(status_code=404, detail="Provider is not found")
    return db_provider


@app.get("/providers/{provider_id}", response_model=schemas.provider.Provider)
def get_provider_api(provider_id: str, db: Session = Depends(get_db)):
    db_provider = get_provider(db, provider_id=provider_id)
    if db_provider is None:
        raise HTTPException(status_code=404, detail="Provider is not found")
    return db_provider


@app.delete("/providers/{provider_id}")
def delete_provider_api(provider_id: str, db: Session = Depends(get_db)):
    db_provider = delete_provider(db, provider_id=provider_id)
    if not db_provider:
        raise HTTPException(status_code=404, detail="Provider is not found")

    return {"message": "provider deleted with success!"}
