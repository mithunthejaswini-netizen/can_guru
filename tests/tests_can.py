import pytest
from can_guru.can.can_classic import CanClassic

def test_std_can_pos_tc_01():
    
    can_classic_frame = CanClassic(0x32, 8, (0, 1, 2, 3, 4, 5, 6, 7))
    assert can_classic_frame.id == 0x32
    assert can_classic_frame.dlc == 8
    assert can_classic_frame.data == (0, 1, 2, 3, 4, 5, 6, 7)

def test_std_can_pos_tc_02():
    
    can_classic_frame = CanClassic(0, 3, (0, 1, 2, 3, 4, 5, 6, 7))
    
    assert can_classic_frame.id == 0
    assert can_classic_frame.dlc == 3
    assert can_classic_frame.data == (0, 1, 2)
    
def test_std_can_pos_tc_03():
    can_classic_frame = CanClassic(0x32, 2, (0, 1, 2, 3, 4, 5, 6, 7))
    
    assert can_classic_frame.id == 0x32
    assert can_classic_frame.dlc == 2
    assert can_classic_frame.data == (0, 1)
    assert can_classic_frame.brs == 1
    assert can_classic_frame.ide == 0
    assert can_classic_frame.fdf == 0
    
def test_std_can_pos_tc_04():
    can_classic_frame = CanClassic(0x12, 5, (0, 1, 2, 3, 4, 5, 6, 7))
    
    can_classic_frame.ide = 1
    can_classic_frame.brs = 0
    
    assert can_classic_frame.id == 0x12
    assert can_classic_frame.dlc == 5
    assert can_classic_frame.data == (0, 1, 2, 3, 4)
    assert can_classic_frame.brs == 0
    assert can_classic_frame.ide == 1
    with pytest.raises(ValueError):
        can_classic_frame.fdf = 1
        assert can_classic_frame.fdf == 1
    
def test_std_can_pos_tc_05():
    
    can_classic_frame = CanClassic(0x12, 5, (0, 1, 2, 3, 4, 5, 6, 7))
    
    can_classic_frame.ide = 1
    can_classic_frame.brs = 0
    
    assert can_classic_frame.id == 0x12
    assert can_classic_frame.dlc == 5
    assert can_classic_frame.data == (0, 1, 2, 3, 4)
    assert can_classic_frame.brs == 0
    assert can_classic_frame.ide == 1
    with pytest.raises(ValueError):
        can_classic_frame.fdf = 1
        assert can_classic_frame.fdf == 1
        
def test_std_can_pos_tc_06():
    
    can_classic_frame = CanClassic(0x7FF, 6, (0, 1, 2, 3, 4, 5, 6))
    
    can_classic_frame.ide = 1
    can_classic_frame.brs = 0
    
    assert can_classic_frame.id == 0x7FF
    assert can_classic_frame.dlc == 6
    assert can_classic_frame.data == (0, 1, 2, 3, 4, 5)
    assert can_classic_frame.brs == 0
    assert can_classic_frame.ide == 1
    with pytest.raises(ValueError):
        can_classic_frame.fdf = 1
        assert can_classic_frame.fdf == 1

def test_std_can_neg_tc_07():
    
    can_classic_frame = CanClassic(0x7FFF, 1, (0, 1, 2, 3, 4, 5, 6), ide=1)
    
    can_classic_frame.ide = 1
    can_classic_frame.brs = 0
    
    assert can_classic_frame.id == 0x7FFF
    assert can_classic_frame.dlc == 1
    assert can_classic_frame.data == (0,)
    assert can_classic_frame.brs == 0
    assert can_classic_frame.ide == 1
    with pytest.raises(ValueError):
        can_classic_frame.fdf = 1
        assert can_classic_frame.fdf == 1
        
def test_std_can_neg_tc_08():
    
    can_classic_frame = CanClassic(0x1FFFFFFF, 1, (0, 1, 2, 3, 4, 5, 6), ide=1)
    
    can_classic_frame.brs = 0
    
    assert can_classic_frame.id == 0x1FFFFFFF
    assert can_classic_frame.dlc == 1
    assert can_classic_frame.data == (0,)
    assert can_classic_frame.brs == 0
    assert can_classic_frame.ide == 1
    with pytest.raises(ValueError):
        can_classic_frame.fdf = 1
        assert can_classic_frame.fdf == 1
        
def test_std_can_neg_tc_09():
    
    with pytest.raises(ValueError):
        can_classic_frame = CanClassic(0x3FFFFFFF, 1, (0, 1, 2, 3, 4, 5, 6), ide=1)
    
        can_classic_frame.brs = 0
            
        assert can_classic_frame.dlc == 1
        assert can_classic_frame.data == (0,)
        assert can_classic_frame.brs == 0
        assert can_classic_frame.ide == 1
        with pytest.raises(ValueError):
            can_classic_frame.fdf = 1
            assert can_classic_frame.fdf == 1
            
def test_std_can_pos_tc_10():
    
    
    can_classic_frame = CanClassic(0x3FF, 1, (0, 1, 2, 3, 4, 5, 6))

    can_classic_frame.ide = 1
    can_classic_frame.brs = 0
        
    assert can_classic_frame.dlc == 1
    assert can_classic_frame.data == (0,)
    assert can_classic_frame.brs == 0
    assert can_classic_frame.ide == 1
    assert can_classic_frame.isStd() == True
    
    with pytest.raises(ValueError):
        can_classic_frame.fdf = 1
        assert can_classic_frame.fdf == 1
        
def test_std_can_pos_tc_11():
    
    can_classic_frame = CanClassic(0x8FFFF, 1, (0, 1, 2, 3, 4, 5, 6), ide=1)

    can_classic_frame.brs = 0
        
    assert can_classic_frame.dlc == 1
    assert can_classic_frame.data == (0,)
    assert can_classic_frame.brs == 0
    assert can_classic_frame.ide == 1
    assert can_classic_frame.isExt() == True
    with pytest.raises(ValueError):
        can_classic_frame.fdf = 1
        assert can_classic_frame.fdf == 1
    