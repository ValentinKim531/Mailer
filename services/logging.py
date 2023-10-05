import logging
from logging.handlers import RotatingFileHandler
from fastapi import Request


logger = logging.getLogger("uvicorn")


def logging_actions():
    logger.setLevel(logging.INFO)
    handler = RotatingFileHandler("app.log", maxBytes=5000000, backupCount=3)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)


async def log_errors(request: Request, call_next):
    response = await call_next(request)
    if response.status_code == 422:
        logger.error(
            f"Error 422: Unprocessable Entity. Path: {request.url.path}"
        )
    return response
