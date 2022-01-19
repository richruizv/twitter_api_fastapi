#Python
from datetime import date,datetime
from typing import Optional
from uuid import UUID

#Pydantic
from pydantic import BaseModel
from pydantic import EmailStr, Field

class User(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(
        ..., 
        min_length=8,
        max_length=64
    )
    first_name : str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)

class Tweet(BaseModel):
    tweet_id: UUID = Field(..., alias="Tweet id")
    content: str = Field(..., min_length=2, max_length=256, example="Hello World")
    created_at: datetime = Field(default=datetime.now())
    updated_at: Optional[datetime] = Field(default=None)
    by: User = Field(..., alias="User")