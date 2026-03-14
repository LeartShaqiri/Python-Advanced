from pydantic import BaseModel
from typing import Optional


Class RecipieBase(BaseModel):
    name: str
    description: str
    ingredients: str
    cooking_time: int
    cuisine: str
    difficulty: str
    category_id:  Optional [int] = None


class RecipieCreate(RecipieBase):

    pass


class Recipie(RecipieBase):
    id: int