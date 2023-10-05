from fastapi import FastAPI, Request
from routes import email_routes
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("uvicorn")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler("app.log", maxBytes=5000000, backupCount=3)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
handler.setFormatter(formatter)

logger.addHandler(handler)

app = FastAPI()

app.include_router(email_routes.router)


@app.middleware("http")
async def log_errors(request: Request, call_next):
    response = await call_next(request)
    if response.status_code == 422:
        logger.error(
            f"Error 422: Unprocessable Entity. Path: {request.url.path}"
        )
    return response
