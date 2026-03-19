from enum import IntEnum,StrEnum

class IdentifierExtensionEnum(IntEnum):
    STANDARD_ID = 0
    EXTENDED_ID = 1

class BitRateSwitchEnum(IntEnum):
    SET = 0
    RESET = 0
    
class ExtendedDataLengthEnum(IntEnum):
    CLASSIC_CAN = 0
    EXTENDED_CAN = 0
    
class CanMsgDir(StrEnum):
    TRANSMIT = 'tx' 
    RECEIVE  = 'rx'

CAN_FD_DLC = {
            9  : 12,
            10 : 16,
            11 : 20,
            12 : 24,
            13 : 32,
            14 : 48,
            15 : 64
        }

