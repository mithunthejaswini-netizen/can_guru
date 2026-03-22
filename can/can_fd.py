from can.can import CAN
from ..utils.can_utils import CAN_FD_DLC_TABLE
from ..utils.can_utils import FlexibleDataRateFormatEnum as FDF
class CanFd(CAN):
    
    def __init__(self):
        super().__init__()
        
    @CAN.dlc.setter
    def dlc(self, dlc):
        
        if dlc < 0 and dlc > 0xF:
            ValueError("DLC should be > 0 and < F")

        can_tx_len = CAN_FD_DLC_TABLE[self._dlc]
        
        if len(self._data) > can_tx_len:
            self._data = self._data[can_tx_len]
            
    @CAN.fdf.setter
    def fdf(self, fdf):
        if fdf in FDF:
            if fdf==FDF.CLASSIC_CAN.value:
                raise ValueError('FDF cannot be zero for Flexible CAN')
            
        self._fdf = fdf        
        
        
