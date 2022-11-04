from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm.collections import attribute_keyed_dict
from sqlalchemy import Integer

from models import Base

# I can't `import x as _x` - seems the `Mapped` type-hint breaks runtime?
# Works if you use change to just `import B` and change the type-hint on line 19
from models.b import B as _B


class A(Base):
    __tablename__ = "A"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    Bs: Mapped[dict[str, _B]] = relationship(
        # Doesn't help if I change this from string form to `_B`, or `lambda: _B`
        "B",
        back_populates="A",
        collection_class=attribute_keyed_dict("name"),
    )
