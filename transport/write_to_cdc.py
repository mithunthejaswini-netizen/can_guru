
import threading
import queue


# -------------------------------
# Task Queue (per thread)
# -------------------------------
class TaskQueue:

    def __init__(self):
        self._queue = queue.Queue()

    def put(self, task: dict):
        self._queue.put(task)

    def get(self, timeout=None):
        return self._queue.get(timeout=timeout)

    def task_done(self):
        self._queue.task_done()

    def wait_completion(self):
        self._queue.join()

# -------------------------------
# Worker Thread
# -------------------------------
class SerialWrite(threading.Thread):

    def __init__(self, task_queue: TaskQueue, stop_event, name=None):
        super().__init__(name=name)
        self.task_queue = task_queue
        self.stop_event = stop_event
        self.daemon = False

    def run(self):
        while not self.stop_event.is_set(): # or not self.task_queue._queue.empty():
            try:
                d = {"type": "print", "message": "Hello from Queue-1"}
                task = self.task_queue.put(d)
                print(f"[{self.name}] put printing {task}")
            except queue.Empty:
                continue

            # try:
            #     print(f"[{self.name}] put printing ",d)
            # finally:
            #     self.task_queue.task_done()
                
class SerialRead(threading.Thread):

    def __init__(self, task_queue: TaskQueue, stop_event, name=None):
        super().__init__(name=name)
        self.task_queue = task_queue
        self.stop_event = stop_event
        self.daemon = False

    def run(self):
        while not self.stop_event.is_set(): # or not self.task_queue._queue.empty():
            try:
                task = self.task_queue.get(timeout=1)  # ⬅ important
            except queue.Empty:
                continue

            try:
                print(f"[{self.name}] get printing {task}")
            finally:
                self.task_queue.task_done()
                
# -------------------------------
# Main (2 threads, 2 queues)
# -------------------------------
if __name__ == "__main__":

    # Two independent queues
    queue1 = TaskQueue()
    queue2 = TaskQueue()
    
    stop_event = threading.Event()
    
    for i in range(10000):
        queue1.put({"type": "print", "message": "Hello from Queue-1"})

    # Two worker threads
    thread1 = SerialWrite(queue1, stop_event, name="Worker-1")
    thread2 = SerialRead(queue1, stop_event, name="Worker-2")

    thread1.start()
    thread2.start()

    # Wait for completion
    queue1.wait_completion()
    #queue2.wait_completion()
    print("All tasks completed")

    queue1.put({"CAN": [32,85]})
    queue1.put({"CAN-FD":[1,2,3,4,5,6]})

    #queue2.put({"CAN": [32,85]})
    #queue2.put({"CAN-FD":[1,2,3,4,5,6]})

    queue1.wait_completion()
    #queue2.wait_completion()

    while True:
        pass
    
    stop_event.set()

    thread1.join()
    thread2.join()
    
    while True:
        pass