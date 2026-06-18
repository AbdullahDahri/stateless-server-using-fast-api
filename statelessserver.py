from fastapi import FastAPI
from pydantic import BaseModel
# pydantic class i used for importing base class which. help us to create the type of data base we want to allowed in post method

app=FastAPI()

class User(BaseModel):
    name:str
    email:str
    age:int
    
@app.get("/")
def home():
    return {"message": "API is working!",
            "Status": "Success"}

@app.post("/users/")
def addusers(user: User):
    newuser={"id":1,"name":user.name,"email":user.email,"age":user.age}
    return newuser