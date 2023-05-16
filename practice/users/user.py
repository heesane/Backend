from typing import List, Optional
from pydantic import BaseModel, Field
from fastapi import APIRouter
class UserBase(BaseModel):
    name:str
    age:int
    
router = APIRouter()

db = []

@router.get("",tags=["user"])
async def get_user():
    if db:
        return db
    else:
        return "No user found"

@router.post("",tags=["user"])
async def create_user(user: dict):
    db.append({"name":user["name"],"age":user["age"]})
    return "db updated"

@router.put("",tags=["user"])
async def update_user(data: dict):
    idx = data["idx"]
    name = data["name"]
    age = data["age"]
    db[idx] = {"name":name,"age":age}
    return "Successfully updated"

@router.delete("",tags=["user"])
async def delete_user(data: dict):
    idx = data["idx"]
    del db[idx]
    return "Successfully deleted"

