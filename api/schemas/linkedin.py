from pydantic import BaseModel

class PostRequest(BaseModel):
    topic: str

class PostResponse(BaseModel):
    content: str
