from pydantic import BaseModel
from datetime import datetime
from pydantic import HttpUrl
class URLCreate(BaseModel):
    original_url : HttpUrl

class URLResponse(URLCreate):
    short_code: str
    hits: int
    class Config:
        from_attributes = True

class URLStats(URLResponse):
    created_at:datetime
    