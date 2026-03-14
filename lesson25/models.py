from pydantic import BaseModel 

class MovieCreate(BaseModel):
    title:str
    director:str
    date: str


class Movies(MovieCreate):
    id: int    

