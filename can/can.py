from ..utils.can_utils import IdentifierExtensionEnum as IDE
from ..utils.can_utils import BitRateSwitchEnum as BRS
from ..utils.can_utils import FlexibleDataRateFormatEnum as FDF
from ..utils.can_utils import CanMsgDir as DIR
from ..utils.can_utils import CAN_ID_RANGE
class CAN:
    def __init__(
                self,
                id,
                dlc,
                data,
                *,
                fdf=FDF.CLASSIC_CAN.value,
                ide=IDE.STANDARD_ID.value,
                dir=DIR.TRANSMIT.value,
                brs=BRS.SET.value                 
            ):
        
        self.id = id
        self.dlc = dlc
        self.data = data
        self.fdf = fdf
        self.dir = dir
        self.brs = brs
        self.ide = ide

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
    def fdf(self):
        return self._fdf
    
    @id.setter
    def id(self, id):
        
        if id < 0:
            raise ValueError("ID should be >0")
        
        if id > CAN_ID_RANGE.EXT_ID_MAX.value:
            raise ValueError("ID value should not exceed > 29bits")
        
        self._id = id
    
    @dlc.setter
    def dlc(self, dlc):
        
        if dlc < 0 or dlc > 8:
            raise ValueError("DLC should be > 0 and < 8")
        self._dlc = dlc

    @dir.setter
    def dir(self, dir):
        
        if dir in DIR:
            self._dir = dir
    
    @fdf.setter
    def fdf(self, fdf):
        
        if fdf in FDF:
            if fdf != FDF.CLASSIC_CAN.value:
                raise ValueError('FDF should be 0 for classic CAN')
        self._fdf = fdf
            
    @ide.setter
    def ide(self, ide):

        if ide in IDE:
            
            if self._id <= CAN_ID_RANGE.STD_ID_MAX.value and ide==0:
                self._ide = ide
            elif self._id <= CAN_ID_RANGE.EXT_ID_MAX.value and ide==1:
                self._ide = ide
            else:
                raise ValueError('IDE and arbitration id should be within range')
        else:
            raise ValueError('IDE should be 0 or 1 i.e. standard or extended identifier')
            
    @brs.setter
    def brs(self, brs):
        
        if brs in BRS:
            self._brs = brs
    
    @data.setter
    def data(self, data):

        if len(data) < self._dlc:
            raise ValueError("Data length is less than DLC")
            
        self._data = data[:self._dlc]
            
    def isStd(self):
        return self._id <= CAN_ID_RANGE.STD_ID_MAX.value
    
    def isExt(self):
        return self._id > CAN_ID_RANGE.STD_ID_MAX.value and \
            self._id <= CAN_ID_RANGE.EXT_ID_MAX.value
    
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