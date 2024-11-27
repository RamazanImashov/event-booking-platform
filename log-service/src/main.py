from fastapi import FastAPI, HTTPException, Depends, Request, Form
from fastapi.templating import Jinja2Templates

from decouple import config

import cloudinary.uploader
# from .db import db, serialize_dict
import uvicorn
from .register import router as register_router
from .archive_logs import router as archive_router


cloudinary.config(
    cloud_name=config("CLOUD_NAME"),
    api_key=config("API_KEY"),
    api_secret=config("API_SECRET")
)


app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(register_router)
app.include_router(archive_router)


@app.get("/")
async def index(request: Request):
    services = await db.services.find().to_list(None)
    return templates.TemplateResponse("index.html", {"request": request, "services": services})


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8007, log_level="info")
