from __future__ import annotations

from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, String

from models import Base

if TYPE_CHECKING:
    # I can't `import x as _x` - seems the `Mapped` type-hint breaks
    # Works if you use change to just `import A` and change the type-hint on line 28
    from models.a import A as _A


class B(Base):
    __tablename__ = "B"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    A_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("A.id"),
        nullable=False,
    )

    A: Mapped["_A"] = relationship(
        "A",
        back_populates="Bs",
    )
