from redis import Redis
from rq import Queue

def hello():
    print("Hello from queue!")

redis_conn = Redis(host="localhost", port=6379, password="own_password")
queue = Queue("task_queue", connection=redis_conn)

job = queue.enqueue(hello)
print(job.id)
