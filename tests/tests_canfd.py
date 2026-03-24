import pytest
from can_guru.can.can_fd import CanFd

def test_std_canfd_pos_tc_01():
    
    can_Fd = CanFd(0x32, 8, tuple(i for i in range(8)), fdf=1)
    assert can_Fd.id == 0x32
    assert can_Fd.dlc == 8
    assert can_Fd.data == tuple(i for i in range(8))

def test_std_canfd_pos_tc_02():
    
    can_Fd = CanFd(0, 13, tuple(i for i in range(32)), fdf=1)
    
    assert can_Fd.id == 0
    assert can_Fd.dlc == 13
    assert can_Fd.data == tuple(i for i in range(32))
    
def test_std_canfd_pos_tc_03():
    can_Fd = CanFd(0x32, 14, tuple(i for i in range(48)), fdf=1)
    
    assert can_Fd.id == 0x32
    assert can_Fd.dlc == 14
    assert can_Fd.data == tuple(i for i in range(48))
    assert can_Fd.brs == 1
    assert can_Fd.ide == 0
    assert can_Fd.fdf == 1
    
def test_std_canfd_pos_tc_04():
    can_classic_frame = CanFd(0x12, 15, tuple(i for i in range(64)), fdf=1)
    
    can_classic_frame.ide = 1
    can_classic_frame.brs = 0
    
    assert can_classic_frame.id == 0x12
    assert can_classic_frame.dlc == 15
    assert can_classic_frame.data == tuple(i for i in range(64))
    assert can_classic_frame.brs == 0
    assert can_classic_frame.ide == 1
    
    with pytest.raises(ValueError):
        can_classic_frame.fdf = 0
        assert can_classic_frame.fdf == 0
    
def test_std_canfd_pos_tc_05():
    
    can_classic_frame = CanFd(0x12, 5, tuple(i for i in range(7)), fdf=1)
    
    can_classic_frame.ide = 1
    can_classic_frame.brs = 0
    
    assert can_classic_frame.id == 0x12
    assert can_classic_frame.dlc == 5
    assert can_classic_frame.data == tuple(i for i in range(5))
    assert can_classic_frame.brs == 0
    assert can_classic_frame.ide == 1
    
    with pytest.raises(ValueError):
        can_classic_frame.fdf = 0
        assert can_classic_frame.fdf == 0
        
def test_std_canfd_pos_tc_06():
    
    can_classic_frame = CanFd(0x7FF, 6, tuple(i for i in range(10)), fdf=1)
    
    can_classic_frame.ide = 1
    can_classic_frame.brs = 0
    
    assert can_classic_frame.id == 0x7FF
    assert can_classic_frame.dlc == 6
    assert can_classic_frame.data == tuple(i for i in range(6))
    assert can_classic_frame.brs == 0
    assert can_classic_frame.ide == 1
    with pytest.raises(ValueError):
        can_classic_frame.fdf = 0
        assert can_classic_frame.fdf == 0

def test_std_canfd_neg_tc_07():
    
    can_classic_frame = CanFd(0x7FFF, 1, (0, 1, 2, 3, 4, 5, 6), fdf=1, ide=1)
    
    can_classic_frame.brs = 0
    
    assert can_classic_frame.id == 0x7FFF
    assert can_classic_frame.dlc == 1
    assert can_classic_frame.data == (0,)
    assert can_classic_frame.brs == 0
    assert can_classic_frame.ide == 1
        
def test_std_canfd_neg_tc_08():
    
    can_classic_frame = CanFd(0x1FFFFFFF, 1, (0, 1, 2, 3, 4, 5, 6), fdf=1, ide=1)
    
    can_classic_frame.brs = 0
    
    assert can_classic_frame.id == 0x1FFFFFFF
    assert can_classic_frame.dlc == 1
    assert can_classic_frame.data == (0,)
    assert can_classic_frame.brs == 0
    with pytest.raises(ValueError):
        can_classic_frame.ide = 0
        
def test_std_canfd_neg_tc_09():
    
    with pytest.raises(ValueError):
        can_classic_frame = CanFd(0x3FFFFFFF, 1, (0, 1, 2, 3, 4, 5, 6), fdf=1, ide=1)
    
        can_classic_frame.ide = 1
        can_classic_frame.brs = 0
            
        assert can_classic_frame.dlc == 1
        assert can_classic_frame.data == (0,)
        assert can_classic_frame.brs == 0
        assert can_classic_frame.ide == 1
            
def test_std_canfd_pos_tc_10():
    
    
    can_classic_frame = CanFd(0x3FF, 1, (0, 1, 2, 3, 4, 5, 6), fdf=1)

    can_classic_frame.ide = 1
    can_classic_frame.brs = 0
        
    assert can_classic_frame.dlc == 1
    assert can_classic_frame.data == (0,)
    assert can_classic_frame.brs == 0
    assert can_classic_frame.ide == 1
    assert can_classic_frame.isStd() == True
        
def test_std_canfd_pos_tc_11():
    
    can_classic_frame = CanFd(0x8FFFF, 1, (0, 1, 2, 3, 4, 5, 6), fdf=1, ide=1)

    can_classic_frame.brs = 0
        
    assert can_classic_frame.dlc == 1
    assert can_classic_frame.data == (0,)
    assert can_classic_frame.brs == 0
    assert can_classic_frame.ide == 1
    assert can_classic_frame.isExt() == True