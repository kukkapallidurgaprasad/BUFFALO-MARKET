from sqlalchemy.orm import Session
from models import Buffalo

def add_buffalo(db: Session, buffalo):
    new_buffalo = Buffalo(**buffalo.dict())
    db.add(new_buffalo)
    db.commit()
    db.refresh(new_buffalo)
    return new_buffalo

def get_all_buffalo(db: Session):
    return db.query(Buffalo).all()

def buy_buffalo(db: Session, buffalo_id: int):
    buffalo = db.query(Buffalo).filter(Buffalo.id == buffalo_id).first()
    if buffalo and buffalo.status == "available":
        buffalo.status = "sold"
        db.commit()
        return buffalo
    return None
