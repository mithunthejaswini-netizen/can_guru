from ..utils.can_utils import CAN_ID_RANGE

class CanSerialBusFormat:
    
    send_to_cdc = False
    receive_from_cdc = False
    
    @classmethod
    def start_sending(cls):
        if not cls.send_to_cdc:
            cls.send_to_cdc = True
        
    @classmethod
    def start_receiving(cls):
        if not cls.receive_from_cdc:
            cls.receive_from_cdc = True