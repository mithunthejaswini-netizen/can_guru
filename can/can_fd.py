class CanStd:
    
    def __init__(self):
        self._brs = 0
        
    @property
    def brs(self):
        return self._brs
    
    @brs.setter
    def brs(self, brs):
        if brs in (0, 1):
            self._brs = brs
        else:
            ValueError('BRS value is out of range')