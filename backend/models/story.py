from sqlalchemy import Column, Interger, String, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from backend.db.database import Base

class Story():
    __tablename__="stories"

    id=Column(Interger, primary_key=True, index=True)
    title=Column(String, index=True)
    session_id=Column(String,index=True)
    created_at=Column(DateTime(timezone=True), server_default=func.now())


    nodes= relationship("StoryNode", back_populates="story")

class Story(Base):
    __tablename__ = "story_nodes"

    id = Column(Interger, primary_key=True,index=True)
    story_id = Column(Interger, ForeignKey("stories.id"), index=True)
    content = Column(String)
    is_root = Column(Boolean, default=False)
    is_ending = Column(Boolean, default=False)
    is_wnning_ending = Column(Boolean, default=False)
    options = Column(JSON, default=list)

    story = relationship("Story", back_populates="nodes")
