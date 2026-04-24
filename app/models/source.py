"""Source sqlalchemy model."""

from typing import TYPE_CHECKING

from sqlalchemy import Boolean
from sqlalchemy import Enum
from sqlalchemy import text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.base import TimeStampMixin
from app.models.enums import SourceType

if TYPE_CHECKING:
    from app.models.news_item import NewsItem


class Source(Base, TimeStampMixin):
    """Source model."""

    __tablename__ = "sources"

    type: Mapped[SourceType] = mapped_column(Enum(SourceType))
    name: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column(unique=True)
    enabled: Mapped[bool] = mapped_column(Boolean, server_default=text("true"))

    news: Mapped[list["NewsItem"]] = relationship(
        "NewsItem",
        back_populates="source",
    )
