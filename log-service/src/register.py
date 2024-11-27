from fastapi import APIRouter, HTTPException
from uuid import uuid4
# from bson import ObjectId
# from db import db, serialize_dict

router = APIRouter(
    prefix="/register",
    tags=["Register"]
)


# Register a new user
@router.post("/register_user")
async def register_user(telegram_id: str, username: str):
    existing_user = db.users.find_one({"telegram_id": telegram_id})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    user = {
        "telegram_id": telegram_id,
        "username": username,
        "services": []
    }
    result = db.users.insert_one(user)
    return {"status": "success", "user_id": str(result.inserted_id)}


# Login a user by Telegram ID
@router.post("/login_user")
async def login_user(telegram_id: str):
    user = db.users.find_one({"telegram_id": telegram_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return serialize_dict(user)


# Register a new service for a user
@router.post("/register_service")
async def register_service(user_id: str, service_name: str):
    service = {
        "name": service_name,
        "api_key": str(uuid4()),
        "user_id": user_id,
        "logs": []
    }
    result = db.services.insert_one(service)
    db.users.update_one({"_id": ObjectId(user_id)}, {"$push": {"services": result.inserted_id}})
    return {"status": "success", "service_id": str(result.inserted_id), "api_key": service["api_key"]}
