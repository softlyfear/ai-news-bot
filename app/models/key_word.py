"""KeyWord sqlalchemy model."""

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.base import Base
from app.models.base import TimeStampMixin


class KeyWord(Base, TimeStampMixin):
    """KeyWord model."""

    __tablename__ = "key_words"

    word: Mapped[str] = mapped_column(unique=True)
