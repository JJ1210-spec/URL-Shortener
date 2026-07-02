
from sqlalchemy import Column , Integer, String, DateTime
from sqlalchemy.orm import declarative_base

from datetime import datetime

Base = declarative_base()
class URL(Base):
    __tablename__ = "URL"
    id =  Column(Integer,primary_key=True,index=True)
    original_url = Column(String)
    short_code = Column(String , unique=True)
    hits= Column(Integer, default=0) 
    created_at = Column(DateTime, default=datetime.utcnow)



