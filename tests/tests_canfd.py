import pytest
from can_guru.can.can_fd import CanFd

def test_std_canfd_pos_tc_01():
    
    can_Fd = CanFd(0x32, 8, tuple(i for i in range(8)), fdf=1)
    assert can_Fd.id == 0x32
    assert can_Fd.dlc == 8
    assert can_Fd.data == tuple(i for i in range(8))
    
    m = list(can_Fd.to_bytes())
    k = ([hex(n) for n in m])

    assert k == ['0x0', '0x1', '0x0', '0x0', '0x0', '0x32', '0x8', '0x0', '0x1', '0x2', '0x3', '0x4', '0x5', '0x6', '0x7']

def test_std_canfd_pos_tc_02():
    
    can_Fd = CanFd(0, 13, tuple(i for i in range(32)), fdf=1)
    
    assert can_Fd.id == 0
    assert can_Fd.dlc == 13
    assert can_Fd.data == tuple(i for i in range(32))
    
    m = list(can_Fd.to_bytes())
    k = ([hex(n) for n in m])
    
    assert k == ['0x0', '0x1', '0x0', '0x0', '0x0', '0x0', '0xd', '0x0', '0x1', '0x2', '0x3', '0x4', '0x5', '0x6', '0x7', '0x8', '0x9', '0xa', '0xb', '0xc', '0xd', '0xe', '0xf', '0x10', '0x11', '0x12', '0x13', '0x14', '0x15', '0x16', '0x17', '0x18', '0x19', '0x1a', '0x1b', '0x1c', '0x1d', '0x1e', '0x1f']
    
def test_std_canfd_pos_tc_03():
    
    can_Fd = CanFd(0x32, 14, tuple(i for i in range(48)), fdf=1)
    
    assert can_Fd.id == 0x32
    assert can_Fd.dlc == 14
    assert can_Fd.data == tuple(i for i in range(48))
    assert can_Fd.brs == 1
    assert can_Fd.ide == 0
    assert can_Fd.fdf == 1
    
def test_std_canfd_pos_tc_04():
    
    can_Fd = CanFd(0x12, 15, tuple(i for i in range(64)), fdf=1)
    can_Fd.ide = 1
    can_Fd.brs = 0
    
    assert can_Fd.id == 0x12
    assert can_Fd.dlc == 15
    assert can_Fd.data == tuple(i for i in range(64))
    assert can_Fd.brs == 0
    assert can_Fd.ide == 1
    
    with pytest.raises(ValueError):
        can_Fd.fdf = 0
        assert can_Fd.fdf == 0
    
def test_std_canfd_pos_tc_05():
    
    can_Fd = CanFd(0x12, 5, tuple(i for i in range(7)), fdf=1)
    can_Fd.ide = 1
    can_Fd.brs = 0
    
    assert can_Fd.id == 0x12
    assert can_Fd.dlc == 5
    assert can_Fd.data == tuple(i for i in range(5))
    assert can_Fd.brs == 0
    assert can_Fd.ide == 1
    
    with pytest.raises(ValueError):
        can_Fd.fdf = 0
        assert can_Fd.fdf == 0
        
def test_std_canfd_pos_tc_06():
    
    can_Fd = CanFd(0x7FF, 6, tuple(i for i in range(10)), fdf=1)
    can_Fd.ide = 1
    can_Fd.brs = 0
    
    assert can_Fd.id == 0x7FF
    assert can_Fd.dlc == 6
    assert can_Fd.data == tuple(i for i in range(6))
    assert can_Fd.brs == 0
    assert can_Fd.ide == 1
    with pytest.raises(ValueError):
        can_Fd.fdf = 0
        assert can_Fd.fdf == 0

def test_std_canfd_neg_tc_07():
    
    can_Fd = CanFd(0x7FFF, 1, (0, 1, 2, 3, 4, 5, 6), fdf=1, ide=1)
    can_Fd.brs = 0
    
    assert can_Fd.id == 0x7FFF
    assert can_Fd.dlc == 1
    assert can_Fd.data == (0,)
    assert can_Fd.brs == 0
    assert can_Fd.ide == 1
    
    m = list(can_Fd.to_bytes())
    k = ([hex(n) for n in m])
    
    assert k == ['0x1', '0x1', '0x0', '0x0', '0x7f', '0xff', '0x1', '0x0']
        
def test_std_canfd_neg_tc_08():
    
    can_Fd = CanFd(0x1FFFFFFF, 1, (0, 1, 2, 3, 4, 5, 6), fdf=1, ide=1)
    can_Fd.brs = 0
    
    assert can_Fd.id == 0x1FFFFFFF
    assert can_Fd.dlc == 1
    assert can_Fd.data == (0,)
    assert can_Fd.brs == 0
    with pytest.raises(ValueError):
        can_Fd.ide = 0
        
def test_std_canfd_neg_tc_09():
    
    with pytest.raises(ValueError):
        can_Fd = CanFd(0x3FFFFFFF, 1, (0, 1, 2, 3, 4, 5, 6), fdf=1, ide=1)
        can_Fd.ide = 1
        can_Fd.brs = 0
            
        assert can_Fd.dlc == 1
        assert can_Fd.data == (0,)
        assert can_Fd.brs == 0
        assert can_Fd.ide == 1
            
def test_std_canfd_pos_tc_10():
    
    can_Fd = CanFd(0x3FF, 1, (0, 1, 2, 3, 4, 5, 6), fdf=1)
    can_Fd.ide = 1
    can_Fd.brs = 0
        
    assert can_Fd.dlc == 1
    assert can_Fd.data == (0,)
    assert can_Fd.brs == 0
    assert can_Fd.ide == 1
    assert can_Fd.isStd() == True
        
def test_std_canfd_pos_tc_11():
    
    can_Fd = CanFd(0x8FFFF, 1, (0, 1, 2, 3, 4, 5, 6), fdf=1, ide=1)

    can_Fd.brs = 0
        
    assert can_Fd.dlc == 1
    assert can_Fd.data == (0,)
    assert can_Fd.brs == 0
    assert can_Fd.ide == 1
    assert can_Fd.isExt() == True
    
def test_std_canfd_pos_tc_12():
    
    can_Fd = CanFd(0x8FFFFF, 12, tuple(i for i in range(24)), fdf=1, ide=1)
    can_Fd.brs = 0
    
    assert can_Fd.dlc == 12
    assert can_Fd.data == tuple(i for i in range(24))
    assert can_Fd.brs == 0
    assert can_Fd.ide == 1
    assert can_Fd.isExt() == True
    m = list(can_Fd.to_bytes())   
    assert m == [1, 1, 0, 143, 255, 255, 12, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]