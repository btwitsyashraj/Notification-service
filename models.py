from pydantic import BaseModel
from enum import Enum

class NotificationType(str, Enum):
    email = "email"
    sms = "sms"
    inapp = "inapp"

class Notification(BaseModel):
    user_id: str
    type: NotificationType
    message: str
