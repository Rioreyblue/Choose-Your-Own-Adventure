from typing import List, Optional, Dict
from datetime import datetime
from pydantic import BaseModel

class StoryOptionsSchema(BaseModel):
    text:str
    node_id: Optional[int] = None

class StoryNodeBase(BaseModel):
    content: str
    is_ending: bool = False
    is_winning_ending: bool = False

class CompleteStoryNodeRespose(StoryNodeBase):
    id: int
    options: List[StoryOptionsSchema]=[]


    class Config:
        from_attributes=True

class StoryBase(BaseModel):
    title: str
    session_id=Optional[str] = None

    class Config:
        from_attributes = True

class CreateStoryRequest(BaseModel):
    theme: str


class CompleteStoryResponse(StoryBase):
    id: int
    created_at: datetime
    root_node: CompleteStoryNodeRespose
    all_nodes: Dict[int, CompleteStoryNodeRespose]

    class Config:
        from_attributes = True