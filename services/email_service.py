import aiosmtplib
import logging
from email.message import EmailMessage
from models.email import Email
import os


logger = logging.getLogger("uvicorn")

SMTP_HOST = os.environ.get("SMTP_HOST", "127.0.0.1")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 2525))


async def send_email_message(email: Email):
    try:
        message = EmailMessage()
        message.set_content(email.message)
        message["Subject"] = email.subject
        message["From"] = "test@mail.com"
        message["To"] = email.to

        async with aiosmtplib.SMTP(hostname=SMTP_HOST, port=SMTP_PORT) as smtp:
            await smtp.send_message(message)

        logger.info(f"Email was sent to {email.to}")
        return True
    except Exception as e:
        logger.error(f"Error when trying to send email: {e}")
        return False
