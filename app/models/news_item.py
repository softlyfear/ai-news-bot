"""NewsItem sqlalchemy model."""

import uuid
from datetime import datetime

from sqlalchemy import UUID
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.base import TimeStampMixin
from app.models.post import Post
from app.models.source import Source


class NewsItem(Base, TimeStampMixin):
    """News model."""

    __tablename__ = "news_items"

    title: Mapped[str] = mapped_column(String(255))
    url: Mapped[str | None] = mapped_column(unique=True)
    summary: Mapped[str] = mapped_column(Text)
    source_id: Mapped[uuid.UUID] = mapped_column(
        UUID,
        ForeignKey("sources.id", ondelete="CASCADE"),
    )
    published_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text("TIMEZONE('utc', now())"),
    )
    raw_text: Mapped[str | None] = mapped_column(Text)

    posts: Mapped[list["Post"]] = relationship(
        "Post",
        back_populates="news_item",
        cascade="all, delete-orphan",
    )

    source: Mapped["Source"] = relationship(
        "Source",
        back_populates="news",
    )
