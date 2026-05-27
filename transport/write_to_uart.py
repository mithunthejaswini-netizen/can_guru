import serial
import time
import threading
import queue
from can_guru.can.can_classic import CanClassic
from can_guru.can.can_fd import CanFd
from can_guru.utils.can_utils import CanMsgDir as DIR
from can_guru.utils.can_utils import CAN_FD_DLC_TABLE

# ----------------------------
# SERIAL OPEN
# ----------------------------
def serial_port(comport, baudrate, timeout):
    return serial.Serial(
        port=comport,
        baudrate=baudrate,
        timeout=timeout
    )

# ----------------------------
# TASK QUEUE
# ----------------------------
class TaskQueue:

    def __init__(self):
        self._queue = queue.Queue()

    def put(self, data):
        self._queue.put(data)

    def get(self, timeout=None):
        return self._queue.get(timeout=timeout)

    def task_done(self):
        self._queue.task_done()

# ----------------------------
# FRAME PARSER THREAD
# ----------------------------
class SerialWrite(threading.Thread):

    SOF = 0x32
    EOF = b'\x85\r\n'

    def __init__(self, task_queue, stop_event, comport, name=None):
        super().__init__(name=name)
        self.task_queue = task_queue
        self.stop_event = stop_event
        self.comport = comport
        self.daemon = False
        self.start()

    def run(self):
        while not self.stop_event.is_set():
            try:
                frame = self.task_queue.get()               
                self.comport.write(frame)
                self.comport.flush()        

            except Exception as e:
                print("RX Error:", e)

# ----------------------------
# MAIN
# ----------------------------
if __name__ == '__main__':

    print('sadananda maharaj')
    port = serial_port('COM4', 115200, 0.01)
    time.sleep(2)
    q = TaskQueue()
    stop_event = threading.Event()
    rx_thread = SerialWrite(q, stop_event, port, name="Worker-1")
    
    frame = bytearray()
    frame.append(0x32)           # SOF
    frame.append(0x00)           # IDE
    frame.append(0x01)           # FDF
    frame.extend([0x00, 0x06, 0x12, 0x51])  # CAN ID
    frame.append(0x08)           # DLC
    frame.extend(b'\x11\x22\x33\x44\x55\x66\x77\x88')
    frame.extend(b'\x85\r\n')    # EOF

    q.put(frame)
    
    frame1 = bytearray()
    frame1.append(0x32)           # SOF
    frame1.append(0x00)           # IDE
    frame1.append(0x01)           # FDF
    frame1.extend([0x00, 0x06, 0x12, 0x52])  # CAN ID
    frame1.append(0x08)           # DLC
    frame1.extend(b'\x01\x02\x03\x04\x05\x06\x07\x08')
    frame1.extend(b'\x85\r\n')    # EOF

    q.put(frame1)
    
    frame2 = bytearray()
    frame2.append(0x32)           # SOF
    frame2.append(0x00)           # IDE
    frame2.append(0x01)           # FDF
    frame.extend([0x00, 0x06, 0x12, 0x53])  # CAN ID
    frame2.append(0x08)           # DLC
    frame2.extend(b'\x31\x32\x33\x34\x35\x36\x37\x38')
    frame2.extend(b'\x85\r\n')    # EOF

    q.put(frame2)
    try:
        while True:
            
            if port.in_waiting:

                response = port.read(port.in_waiting)
                print("[RX]", response.hex())
            
            time.sleep(0.1)

    except KeyboardInterrupt:

        stop_event.set()

        port.close()

        print("Stopped")


