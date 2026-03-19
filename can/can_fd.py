from can.can import CAN
from utils.can_utils import CAN_FD_DLC_TABLE
class CanStd(CAN):
    
    def __init__(self):
        super().__init__()
        
    @CAN.dlc.setter
    def dlc(self, dlc):
        
        if dlc < 0 and dlc > 0xF:
            ValueError("DLC should be > 0 and < F")

        can_tx_len = CAN_FD_DLC_TABLE[self._dlc]
        
        if len(self._data) > can_tx_len:
            self._data = self._data[can_tx_len]
            
        
        
        
