from can.can import CAN


if __name__=='__main__':
    can = CAN(3285, 8, (56, 0, 51, 32, 85, 12, 32, 45))
    
    print(can)