from pydantic import BaseModel
from typing import Optional


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class Category(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True