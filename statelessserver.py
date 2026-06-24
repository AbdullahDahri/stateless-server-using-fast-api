from fastapi import FastAPI
from pydantic import BaseModel
# pydantic class i used for importing base class which. help us to create the type of data base we want to allowed in post method

app=FastAPI()
users=[{"id":1,"name":"Abdullah","email":"abdullah@gmail.com","age":30},{"id":2,"name":"Ali","email":"ali@gmail.com","age":25}]

class User(BaseModel):
    user_id:int
    name:str
    email:str
    age:int
    
@app.get("/")
def home():
    return {"message": "API is working!",
            "Status": "Success"}

@app.get("/users/")
def getusers():
    return users
@app.get("/users/{user_id}")
def getuser(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return {"message": "User not found"}

@app.post("/users/")
def addusers(user: User):
    newuser={"id":1,"name":user.name,"email":user.email,"age":user.age}
    return newuser