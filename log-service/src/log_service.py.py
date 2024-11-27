from fastapi import APIRouter, HTTPException, Request
from datetime import datetime
from bson import ObjectId
# from db import db

router = APIRouter(
    prefix="/logs",
    tags=["Logs"]
)


# Add a log entry
@router.post("/")
async def add_log(service_api_key: str, log_level: str, log_message: str):
    service = db.services.find_one({"api_key": service_api_key})
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")

    log = {
        "log_level": log_level,
        "log_message": log_message,
        "time": datetime.utcnow()
    }
    db.services.update_one({"_id": service["_id"]}, {"$push": {"logs": log}})
    return {"status": "success"}


# View logs for a specific service
@router.get("/service/{service_id}")
async def service_logs(service_id: str, request: Request):
    service = db.services.find_one({"_id": ObjectId(service_id)})
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return {"service_name": service["name"], "logs": service["logs"]}
