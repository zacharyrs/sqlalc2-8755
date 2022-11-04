from __future__ import annotations

from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, String

from models import Base

if TYPE_CHECKING:
    # Really I want to do `import A as _A` here too.
    from models.a import A


class B(Base):
    __tablename__ = "B"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    A_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("A.id"),
        nullable=False,
    )

    A: Mapped["A"] = relationship(
        "A",
        back_populates="Bs",
    )
