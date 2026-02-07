from celery import Celery
import time
import os

celery_app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task(bind=True)
def process_file(self, filename):
    print(f"Received task: tasks.process_file")
    print(f"Processing file: {filename}")

    time.sleep(5)   # simulate heavy work

    print("Finished processing")
    return "Done"
