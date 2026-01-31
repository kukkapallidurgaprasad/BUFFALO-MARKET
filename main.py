from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from fastapi.middleware.cors import CORSMiddleware
import crud, schemas

app = FastAPI(title="Buffalo Buy & Sell API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# SELL BUFFALO
@app.post("/sell")
def sell_buffalo(buffalo: schemas.BuffaloCreate, db: Session = Depends(get_db)):
    return crud.add_buffalo(db, buffalo)

# VIEW ALL BUFFALO
@app.get("/buffalo")
def list_buffalo(db: Session = Depends(get_db)):
    return crud.get_all_buffalo(db)

# BUY BUFFALO
@app.post("/buy")
def buy_buffalo(data: schemas.BuffaloBuy, db: Session = Depends(get_db)):
    buffalo = crud.buy_buffalo(db, data.buffalo_id)
    if not buffalo:
        raise HTTPException(status_code=404, detail="Buffalo not available")
    return buffalo
