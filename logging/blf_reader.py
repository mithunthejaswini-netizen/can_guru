import can

def read_blf(filename='CAN__CANFD.blf'):
    reader = can.BLFReader(filename)

    for msg in reader:
        
        if hasattr(msg, "arbitration_id"):
            if msg.is_fd:
                print("CAN FD")
                print("Timestamp             : ", msg.timestamp)
                print("Channel               : ", msg.channel)
                print("ID                    : ", hex(msg.arbitration_id))
                print("Extended  Flag        : ", msg.is_extended_id)
                print("Bit Rate Switch       : ",msg.bitrate_switch)
                print("Error State Indicator : ",msg.error_state_indicator)
                print("FD Frame              : ", msg.is_fd)
                print("DLC                   : ", msg.dlc)
                print("Data                  : ", msg.data.hex(" "))
                print("Rx/Tx                 : ", "RX" if msg.is_rx else "TX")    
            else:
                print("CAN")
                print("Timestamp                   : ", msg.timestamp)
                print("Channel                     : ", msg.channel)
                print("ID                          : ", hex(msg.arbitration_id))
                print("Extended Flag               : ", msg.is_extended_id)
                print("Remote Transmission Request : ", msg.is_remote_frame)                  
                print("Error Message Flag          : ", msg.is_error_frame)                              
                print("DLC                         : ", msg.dlc)
                print("Data                        : ", msg.data.hex(" "))
                print("Rx/Tx                       : ", "RX" if msg.is_rx else "TX")
            
            print("-" * 40)

if __name__ == "__main__":
    read_blf()