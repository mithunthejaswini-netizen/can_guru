import serial
import time
import serial.tools.list_ports

print(serial.__file__)

# Open CDC serial port
ser = serial.Serial(
    port='COM3',        # Windows → COM3, Linux → /dev/ttyACM0
    baudrate=115200,   # Baudrate is ignored for USB CDC but still required
    timeout=3
)

time.sleep(2)   # allow MCU reset

'''
without loop is there any way to read it.
while True:
    line = ser.readline()
    if line:
        print("RX:", line.decode(errors='ignore').strip())
'''

line = ser.readline()
print("RX:", line.decode(errors='ignore').strip())

# Give time for device reset (important for many MCUs)
time.sleep(2)

# Sample bytes to send
data = bytes([0xAA, 0x55, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06])

# Send data
ser.write(data)

print("Sent:", data)

# Optional: flush to ensure immediate transfer
ser.flush()

ports = serial.tools.list_ports.comports()

for port in ports:
    print("Device:", port.device)
    print("Name:", port.name)
    print("Description:", port.description)
    print("HWID:", port.hwid)
    print("-" * 40)

ser.close()