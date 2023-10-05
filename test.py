from fastapi.testclient import TestClient
from main import app
import os

os.environ["SMTP_HOST"] = "127.0.0.1"
os.environ["SMTP_PORT"] = "2525"

client = TestClient(app)


def test_send_email():
    response = client.post("/send_email", json={
        "to": "test@example.com",
        "subject": "Test about error 200",
        "message": "Hello! This is a test message from application 'Email to client app'"
    })
    assert response.status_code == 200
    assert response.json() == {"status": "Successfully sent"}


def test_send_email_invalid_email():
    response = client.post("/send_email", json={
        "to": "invalid-email",
        "subject": "Test message about error 422",
        "message": "Hello! This is a test message from application 'Email to client app'"
    })
    assert response.status_code == 422

