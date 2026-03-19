from utils.can_utils import DIR, BRS, CanType
from can.can import CAN
class CanStd(CAN):
    
    def __init__(self):
        super().__init__()