from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declared_attr, declarative_base


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)


class Pep(Base):
    number = Column(Integer, unique=True)
    name = Column(String(400))
    status = Column(String(50))
