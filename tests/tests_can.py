import pytest
from can_guru.can.can_std import CanStd

def test_std_can_pos_tc_01():
    
    can_std_frame = CanStd(0x32, 8, (0, 1, 2, 3, 4, 5, 6, 7))
    assert can_std_frame.id == 0x32
    assert can_std_frame.dlc == 8
    assert can_std_frame.data == (0, 1, 2, 3, 4, 5, 6, 7)

def test_std_can_pos_tc_02():
    
    can_std_frame = CanStd(0, 3, (0, 1, 2, 3, 4, 5, 6, 7))
    
    assert can_std_frame.id == 0
    assert can_std_frame.dlc == 3
    assert can_std_frame.data == (0, 1, 2)
    
def test_std_can_pos_tc_03():
    can_std_frame = CanStd(0x32, 2, (0, 1, 2, 3, 4, 5, 6, 7))
    
    assert can_std_frame.id == 0x32
    assert can_std_frame.dlc == 2
    assert can_std_frame.data == (0, 1)
    assert can_std_frame.brs == 1
    assert can_std_frame.ide == 0
    assert can_std_frame.edl == 0
    
def test_std_can_pos_tc_04():
    can_std_frame = CanStd(0x12, 5, (0, 1, 2, 3, 4, 5, 6, 7))
    
    can_std_frame.ide = 1
    can_std_frame.edl = 1
    can_std_frame.brs = 0
    
    assert can_std_frame.id == 0x12
    assert can_std_frame.dlc == 5
    assert can_std_frame.data == (0, 1, 2, 3, 4)
    assert can_std_frame.brs == 0
    assert can_std_frame.ide == 1
    assert can_std_frame.edl == 1