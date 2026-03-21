from enum import IntEnum, StrEnum, auto

class CanFdDLC(IntEnum):
    CAN_FD_DLC_9  = 9
    CAN_FD_DLC_A  = auto()
    CAN_FD_DLC_B  = auto()
    CAN_FD_DLC_C  = auto()
    CAN_FD_DLC_D  = auto()
    CAN_FD_DLC_E  = auto()
    CAN_FD_DLC_F  = auto()
class IdentifierExtensionEnum(IntEnum):
    STANDARD_ID = 0
    EXTENDED_ID = 1
class BitRateSwitchEnum(IntEnum):
    SET = 1
    NOTSET = 0
class ExtendedDataLengthEnum(IntEnum):
    CLASSIC_CAN = 0
    FLEXIBLE_CAN = 1
class CanMsgDir(StrEnum):
    TRANSMIT = 'tx' 
    RECEIVE  = 'rx'

CAN_FD_DLC_TABLE = {
                CanFdDLC.CAN_FD_DLC_9.value  : 12,
                CanFdDLC.CAN_FD_DLC_A.value : 16,
                CanFdDLC.CAN_FD_DLC_B.value : 20,
                CanFdDLC.CAN_FD_DLC_C.value : 24,
                CanFdDLC.CAN_FD_DLC_D.value : 32,
                CanFdDLC.CAN_FD_DLC_E.value : 48,
                CanFdDLC.CAN_FD_DLC_F.value : 64
        }

