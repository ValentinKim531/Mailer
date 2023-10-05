from fastapi import FastAPI, Request
from routes import email_routes
from services import logging
from services.logging import log_errors

logging.logging_actions()


app = FastAPI()

app.middleware("http")(log_errors)
app.include_router(email_routes.router)

