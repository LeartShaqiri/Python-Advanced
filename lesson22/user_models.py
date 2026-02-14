from pydantic import BaseModel, conint, constr

class User(BaseModel):
    id: int
    name: str
    age: int = 0
    email:str  = "wsg@gmail.com"


user = User(id=1, name="14",)
print(user)

class AnotherUser(BaseModel):
    id: conint(gt=50)
    name: constr(min_length=2, max_length=60)

user1 = AnotherUser(id=51, name="jafa")   
print(user1) 

