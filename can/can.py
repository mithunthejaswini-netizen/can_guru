from utils.can_utils import IdentifierExtensionEnum as IDE
from utils.can_utils import BitRateSwitchEnum as BRS
from utils.can_utils import ExtendedDataLengthEnum as EDL
from utils.can_utils import CanMsgDir as DIR

class CAN:
    def __init__(
                self,
                id,
                dlc,
                data,
                *,
                dir=DIR.TRANSMIT.value,
                brs=BRS.SET.value,
                ide=IDE.STANDARD_ID.value,
                edl=EDL.CLASSIC_CAN.value 
            ):
        
        self._id = id
        self._dlc = dlc
        self._data = data
        self._dir = dir
        self._brs = brs
        self._ide = ide
        self._edl = edl

    @property
    def id(self):
        return self._id
    
    @property
    def dlc(self):
        return self._dlc
    
    @property
    def dir(self):
        return self._dir
    
    @property
    def brs(self):
        return self._brs
    
    @property
    def ide(self):
        return self._ide
    
    @property
    def data(self):
        return self._data
    
    @property
    def edl(self):
        return self._edl
    
    @id.setter
    def id(self, id):
        if id < 0:
            ValueError("ID should be >0")
        self._id = id
    
    @dlc.setter
    def dlc(self, dlc):
        if dlc < 0 or dlc > 8:
            ValueError("DLC should be > 0 and < 8")
        self._dlc = dlc

    @dir.setter
    def dir(self, dir):
        if dir in DIR:
            self._dir = dir
    
    @edl.setter
    def edl(self, edl):
        if edl in EDL:
            self._edl = edl
            
    @ide.setter
    def ide(self, ide):
        if ide in IDE:
            self._ide = ide
    
    @data.setter
    def data(self, data):
        if self.data != data:
            self.data = data
            
    def __str__(self):
    
        can_type = 'Extended-CAN :' if self.edl else 'Classic CAN :'
        return (
            f"{can_type}\n"
            f"  can-id   = {hex(self._id)} dec={(self._id)}\n"
            f"  can-dir  = {self._dir}\n"
            f"  can-dlc  = {self._dlc}\n"
            f"  can-brs  = {self._brs}\n"
            f"  can-data = {self._data}\n"
        )