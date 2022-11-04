from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.collections import attribute_keyed_dict
from sqlalchemy import Integer

from models import Base
from models.b import B as _B


class A(Base):
    __tablename__ = "A"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    Bs: Mapped[dict[str, _B]] = relationship(
        "B",
        back_populates="A",
        collection_class=attribute_keyed_dict("name"),
    )
