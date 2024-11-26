# main.py (FastAPI)
import logging
from fastapi import FastAPI, Request, Depends
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, FileResponse
from .routers.event_routers import router as event_router
from .routers.tags_routers import router as tags_router
from pydantic import ValidationError
from starlette import status
import uvicorn
from traceback import format_exc


logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

handler = logging.FileHandler("error.log", mode="a")
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(handler)


app = FastAPI()


app.include_router(event_router)
app.include_router(tags_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8003, log_level="info")
