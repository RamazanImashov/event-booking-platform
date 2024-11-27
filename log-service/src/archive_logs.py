from fastapi import APIRouter
from datetime import datetime
import asyncio
import cloudinary
import cloudinary.uploader
# from db import db

router = APIRouter(
    prefix="/archive_logs",
    tags=["Archive"]
)

# Cloudinary configuration
cloudinary.config(
    cloud_name="your_cloud_name",
    api_key="your_api_key",
    api_secret="your_api_secret"
)


# Periodic archiving task
@router.on_event("startup")
async def archive_logs():
    async def archive():
        while True:
            services = db.services.find()
            for service in services:
                if service["logs"]:
                    log_filename = f"{service['name']}_logs_{datetime.utcnow().strftime('%Y-%m-%d')}.txt"
                    with open(log_filename, "w") as f:
                        for log in service["logs"]:
                            f.write(f"{log['time']} [{log['log_level']}] {log['log_message']}\n")

                    # Upload log file to Cloudinary
                    cloudinary.uploader.upload(
                        log_filename,
                        folder="log_archives",
                        public_id=f"{service['name']}_{datetime.utcnow().strftime('%Y-%m-%d')}"
                    )

                    # Clear logs in the database
                    db.services.update_one({"_id": service["_id"]}, {"$set": {"logs": []}})

            await asyncio.sleep(86400)  # Run daily

    asyncio.create_task(archive())
