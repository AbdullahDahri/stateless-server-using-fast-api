from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# pydantic class i used for importing base class which. help us to create the type of data base we want to allowed in post method

app=FastAPI()
users=[{"id":1,"name":"Abdullah","email":"abdullah@gmail.com","age":30},{"id":2,"name":"Ali","email":"ali@gmail.com","age":25}]
class forpatch(BaseModel):
    name:Optional[str]=None
    email:Optional[str]=None
    age:Optional[int]=None

class User(BaseModel):
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
    newuser={"id":len(users)+1,"name":user.name,"email":user.email,"age":user.age}
    for mail in users:
        if mail["email"]== user.email:
            return{"reasponse":"User Already Exist!"}
    users.append(newuser)
    return {"response":"User added successfully","user":newuser}

@app.delete("/users/{user_id}")
def deleteusers(user_id:int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return{"response":"User deleted successfully"}
    else:
            return{"response":"Invalid user Id, User Not Exist"}
@app.put("/users/{user_id}")
def updteusers(user_id: int, user: User):

    for updateitem in users:
        if updateitem["id"]==user_id:

            updateitem["email"]=user.email
            updateitem["name"]=user.name
            updateitem["age"]=user.age
            return{"response":"User updated successfully","user":updateitem}
    else:
        return{"response":"User not found"}
    

@app.patch("/user/{user_id}")
def updatespecificitem(user_id:int,user:forpatch):
    for updateitem in users:
        if updateitem["id"]==user_id:
            if user.name is not None:
                updateitem["name"]=user.name
            if user.email is not None:
                updateitem["email"]=user.email
            if user.age is not None:
               updateitem["age"]=user.age
            return{"response":"User updated successfully","user":updateitem}
    else:
            return{"response":"User not found"}
               
               
           