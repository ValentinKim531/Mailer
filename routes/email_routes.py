from fastapi import APIRouter, HTTPException
from models.email import Email
from services.email_service import send_email_message
import logging

router = APIRouter()
logger = logging.getLogger("uvicorn")


@router.post("/send_email")
async def send_email_endpoint(email: Email):
    success = await send_email_message(email)
    if not success:
        logger.error(f"Unable to send email to {email.to}")
        raise HTTPException(status_code=500, detail="Email cannot be sent")
    logger.info(f"Email was successfully sent to {email.to}")
    return {"status": "Successfully sent"}
