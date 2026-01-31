from sqlalchemy import Column, Integer, String, Float
from database import Base

class Buffalo(Base):
    __tablename__ = "buffalo"

    id = Column(Integer, primary_key=True, index=True)
    breed = Column(String(50))
    age = Column(Integer)
    milk_per_day = Column(Float)
    price = Column(Float)
    status = Column(String(20), default="available")  # available / sold
