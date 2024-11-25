# main.py (FastAPI)
from fastapi import FastAPI, Request, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationException
from fastapi.responses import JSONResponse, FileResponse
from .routers.event_routers import router as event_router
from .routers.tags_routers import router as tags_router
from pathlib import Path
import uvicorn
import os


app = FastAPI()


# @app.exception_handler(ValidationException)
# async def validation_exception_handler(request: Request, exc:ValidationException):
#     return JSONResponse(
#         status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#         content=jsonable_encoder({"detail": exc.errors()})
#     )


# @app.get("/ads/openapi.json", include_in_schema=False)
# async def get_openapi_json():
#     return FileResponse(os.path.join(os.getcwd(), "openapi.json"))


app.include_router(event_router)
app.include_router(tags_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8003, log_level="info")
