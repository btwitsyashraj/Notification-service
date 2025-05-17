import time

queue = []

def add_to_queue(notification):
    queue.append(notification)
    print(f"Notification added to queue: {notification}")

def process_queue():
    retries = 3
    while queue:
        notification = queue.pop(0)
        for attempt in range(1, retries + 1):
            try:
                # Simulate sending notification
                print(f"Attempt {attempt}: Sending notification {notification}")
                # Fake random failure
                if notification.get("type") == "fail":  
                    raise Exception("Simulated failure")
                print("Notification sent successfully!")
                break  # break retry loop on success
            except Exception as e:
                print(f"Failed to send notification: {e}")
                if attempt == retries:
                    print("Max retries reached. Giving up.")
                else:
                    print("Retrying...")
                    time.sleep(1)
