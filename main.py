from fastapi import FastAPI
from models import Notification
from queue_manager import add_to_queue, process_queue

app = FastAPI()

notifications_db = []

@app.post("/notifications")
def send_notification(notification: Notification):
    notifications_db.append(notification)
    add_to_queue(notification.dict())
    process_queue()  # Immediately process queue for demo; real system async hota hai
    return {"message": "Notification added to queue and processed!"}
