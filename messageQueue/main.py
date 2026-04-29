
from fastapi import FastAPI
from rq import Queue
from redis import Redis
from pydantic import BaseModel
from job import printNumber

app = FastAPI()
redis_conn = Redis(
    host="localhost",
    password="Ghimires@123",
    decode_responses=True,
    port=6379, 
    db=0
    )

task_queue = Queue("task_queue", connection=redis_conn)

class JobRequest(BaseModel):
    lowest: int
    highest: int

@app.get("/")
def index():
    return {
        "success": True,
        "message": "pong"
        }

@app.post("/add-job")
def add_job(job_request: JobRequest):
    job = task_queue.enqueue(printNumber, job_request.lowest, job_request.highest)
    return {
        "success": True,
        "message": f"Job added to queue with ID: {job.id}"
    }