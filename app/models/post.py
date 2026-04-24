"""Post sqlalchemy model."""

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import Text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.models.base import Base
from app.models.base import TimeStampMixin
from app.models.enums import PostStatus

if TYPE_CHECKING:
    from app.models.news_item import NewsItem


class Post(Base, TimeStampMixin):
    """Post model."""

    __tablename__ = "posts"

    news_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("news_items.id", ondelete="CASCADE"),
        index=True,
    )
    generated_text: Mapped[str | None] = mapped_column(Text)
    published_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), index=True
    )
    status: Mapped[PostStatus] = mapped_column(Enum(PostStatus), index=True)

    news_item: Mapped["NewsItem"] = relationship(
        "NewsItem",
        back_populates="posts",
        cascade="all, delete-orphan",
    )
