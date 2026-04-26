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
class SerialRead(threading.Thread):

    SOF = 0x32
    EOF = b'\x85\r\n'

    def __init__(self, task_queue, stop_event, comport, name=None):
        super().__init__(name=name)
        self.task_queue = task_queue
        self.stop_event = stop_event
        self.comport = comport
        self.buffer = bytearray()
        self.daemon = False
        self.start()

    def run(self):

        while not self.stop_event.is_set():

            try:
                if self.comport.in_waiting:

                    data = self.comport.read(self.comport.in_waiting)

                    if data:
                        self.buffer.extend(data)

                    self.extract_frames()

            except Exception as e:
                print("RX Error:", e)

    # ----------------------------
    # EXTRACT COMPLETE FRAMES
    # ----------------------------
    def extract_frames(self):

        while True:

            # search start byte
            sof_index = self.buffer.find(bytes([self.SOF]))

            if sof_index == -1:
                self.buffer.clear()
                return

            # remove junk before SOF
            if sof_index > 0:
                del self.buffer[:sof_index]

            # search EOF sequence
            eof_index = self.buffer.find(self.EOF)

            if eof_index == -1:
                return

            # complete frame found
            frame_end = eof_index + len(self.EOF)

            frame = bytes(self.buffer[:frame_end])

            del self.buffer[:frame_end]
            print(f'received', frame.hex())
            self.task_queue.put(frame)

# ----------------------------
# MAIN
# ----------------------------
if __name__ == '__main__':

    print('sadananda maharaj')
    port = serial_port('COM4', 115200, 0.01)
    time.sleep(2)
    q = TaskQueue()
    stop_event = threading.Event()
    rx_thread = SerialRead(q, stop_event, port, name="Worker-1")

    try:
        
        while True:
            try:        
                frame = q.get(timeout=1)
                #print("[TX] Sending:", frame.hex())
                
                if frame[2]==1:
                    ide = frame[1]
                    fdf = frame[2]
                    id =  (frame[3] << 24) 
                    id = id | frame[4] << 16
                    id = id | frame[5] << 8
                    id = id | frame[6]
                    dlc = frame[7]
                    
                    length = CAN_FD_DLC_TABLE[dlc] + 8

                    data = frame[8: length]           
                    canfd = CanFd( id,
                                dlc,
                                data,
                                fdf=fdf,
                                ide=ide,
                                dir=DIR.RECEIVE.value,
                                brs=1
                            )
                    
                    print('data', data.hex())
                q.task_done()
                
            except queue.Empty:
                continue

    except KeyboardInterrupt:
        stop_event.set()
        print("Stopped")