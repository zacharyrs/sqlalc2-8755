from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


from models.a import A as _A
from models.b import B as _B
