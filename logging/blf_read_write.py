import can
import time

def create_blf():
    # BLF writer from python-can
    writer = can.BLFWriter("demo.blf")
    # ----------------------------
    # Normal CAN Message
    # ----------------------------

    msg1 = can.Message(
                timestamp=time.time(),
                channel=0,
                arbitration_id=0x32,
                is_extended_id=False,
                is_remote_frame=False,
                is_error_frame=False,                              
                dlc=8,
                data=[1,2,3,4,5,6,7,8]                 
    )
    
    writer.on_message_received(msg1)
    time.sleep(0.01)

    # ----------------------------
    # CAN FD Message
    # ----------------------------
    msg2 = can.Message(
        timestamp=time.time(),
        channel=1,
        arbitration_id= 0x3285,
        is_extended_id=True,
        bitrate_switch=True,
        error_state_indicator=False,
        is_fd=True,
        dlc=64,
        data = [i for i in range(64)]
    )

    writer.on_message_received(msg2)
    # close file
    writer.stop()
    print("demo.blf created successfully")


if __name__ == "__main__":    
    create_blf()