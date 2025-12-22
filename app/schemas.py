from typing import Optional
from pydantic import BaseModel, Field

class ItemUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1)
    quantity: Optional[int] = Field(default=None, ge=0)

class ItemCreate(BaseModel):
    name: str = Field(min_length=1)
    quantity: int = Field(ge=0)

class ItemOut(BaseModel):
    id: int
    name: str
    quantity: int

    class Config:
        from_attributes = True
