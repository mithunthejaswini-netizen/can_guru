import serial
import time
import serial.tools.list_ports
import threading
import queue

def serial_port(comport, _baudrate, _timeout):

    # Open CDC serial port
    open_port = serial.Serial(
        port = comport,        # Windows → COM3
        baudrate = _baudrate,   # Baudrate is ignored for USB CDC but still required
        timeout = _timeout
    )
    
    return open_port

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

class SerialRead(threading.Thread):

    def __init__(self, task_queue: TaskQueue, stop_event, comport,  name=None):
        super().__init__(name=name)
        self.task_queue = task_queue
        self.stop_event = stop_event
        self.comport = comport
        self.daemon = False
        self.start()

    def run(self):
        
        while True: #not self.stop_event.is_set(): # or not self.task_queue._queue.empty():
            try:
                if self.comport.in_waiting:
                    data = self.comport.read(self.comport.in_waiting)
                    self.task_queue.put(data)
            
            except queue.Empty:
                continue
        
if __name__=='__main__':
    
    port = serial_port('COM4', 115200, 0.01)
    time.sleep(2)   # allow MCU reset
    queue = TaskQueue()
    stop_event = threading.Event()
    thread = SerialRead(queue, stop_event, port,  name="Worker-1")
    
    while True:
        
        try:
            
            frame = queue.get(timeout=0.01)
            print(f"[TX] Sending: {frame.hex()}")
            # simulate sending
            time.sleep(0.01)
            queue.task_done()
            
        except queue.Empty:
                continue

        time.sleep(0.01)
    