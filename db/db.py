from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,String,Integer,Column,Date
from sqlalchemy.orm import sessionmaker,scoped_session
import os

BASE_DIR=os.path.dirname(os.path.realpath(__file__))
connect_str="sqlite:///" + os.path.join(BASE_DIR,'posts.db')
Base=declarative_base()
engine=create_engine(connect_str,echo=True)
session=scoped_session(
    sessionmaker(bind=engine)
)
Base.query=session.query_property()

class catprefijos(Base):
    __tablename__="catprefijos"
    keyx=Column(Integer(),primary_key=True)
    fechaalta=Column(Date())
    prefijo=Column(String(40))
    def __repr__(self):
        return f"<prefijo {self.prefijo}>"