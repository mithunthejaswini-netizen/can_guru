from utils.can_utils import DIR, BRS

class CAN:
    def __init__(self, ):
        self._id = 0
        self._dlc = 0
        self._data = tuple()
        self._dir = ''
        self._brs = 0 

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
    def data(self):
        return self._data
    
    @id.setter
    def id(self, id):
        if id < 0:
            ValueError("ID should be >0")
        self._id = id
    
    @dlc.setter
    def dlc(self, dlc):
        if dlc < 0:
            ValueError("DLC should be >0")
        self._dlc = dlc

    @dir.setter
    def dir(self, dir):
        if dir in DIR:
            self.dir = dir
    
    @data.setter
    def data(self, data):
        if self.data != data:
            self.data = data