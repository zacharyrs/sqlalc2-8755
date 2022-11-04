from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, String

from models import Base

if TYPE_CHECKING:
    # from models.a import A as A  # works
    from models.a import A as A_alias  # fails


class B(Base):
    __tablename__ = "B"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    A_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("A.id"),
        nullable=False,
    )

    A: Mapped["A_alias"] = relationship(
        "A",
        back_populates="Bs",
    )
