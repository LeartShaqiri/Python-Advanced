from pydantic import BaseModel



class CategoryResponse(BaseModel):
    id: int
    name: str

class Category(BaseModel):
    id: int

class CategoryCreate(CategoryBase):

    pass 

