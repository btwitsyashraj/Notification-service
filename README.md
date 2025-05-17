Notification Service

Introduction
This is a simple Notification Service built to send notifications to users through multiple channels including Email, SMS, and In-App messages. It supports adding notifications via an API and retrieving notifications for a user. The system also includes a basic queue and retry mechanism for processing notifications reliably.

Tech Stack Used
- Python 3.9+
- FastAPI — Web framework for building APIs
- Uvicorn — ASGI server to run FastAPI
- Standard Python libraries for queue and retry logic (no external message broker)

Features
- POST /notifications: Endpoint to send notifications
- GET /users/{id}/notifications: Endpoint to get all notifications for a user
- Supports three notification types: Email, SMS, In-App (simulated by console output)
- Simple in-memory queue system with retries for failed notifications

Setup Instructions

1. Clone the repository or download the project folder.

2. Create a Python virtual environment:

python -m venv venv

3. Activate the Virtual Environment

Activate your Python virtual environment using the command appropriate for your operating system:

- On Windows:

.
env\Scripts\activate

- On macOS/Linux:

source venv/bin/activate

4. Install the required packages:

pip install fastapi uvicorn

5. Run the application server:

uvicorn main:app --reload

6. Open your browser and navigate to the API docs for testing:

http://127.0.0.1:8000/docs

How to Use

Sending a Notification (POST /notifications)

Send a POST request to /notifications with JSON body like:

{
  "user_id": "123",
  "type": "email",
  "message": "Hello, this is a test notification!"
}

Supported type values are: "email", "sms", "inapp".

Getting User Notifications (GET /users/{id}/notifications)

Send a GET request to /users/123/notifications (replace 123 with user ID) to retrieve all notifications sent to that user.

Assumptions

- This project simulates sending notifications by printing messages to the console instead of integrating real email or SMS services.
- Queue and retry mechanisms are implemented in-memory without using external message brokers.
- Notifications are stored temporarily in memory and will reset when the server restarts.

Future Improvements

- Integrate real email and SMS sending services (e.g., SMTP, Twilio).
- Use a persistent database (like PostgreSQL or MongoDB) to store notifications.
- Implement real message queues (RabbitMQ, Kafka) for better scalability.
- Add asynchronous processing for handling notifications.
- Add authentication and authorization for API security.

Live API Documentation

You can test the API endpoints here:

[Notification Service API Docs](https://notification-service-5g5p.onrender.com/docs)

Author
YASH RAJ (Internship Assignment)
