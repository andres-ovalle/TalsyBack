from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id: Optional[str]
    name: str = Field(..., example="John Doe")
    email: str = Field(..., example="john.doe@example.com")
    age: Optional[int] = Field(None, example=30)
