from rehearsal.if_N import if_N

def test_NO():
    assert if_N(6,-2) == 'NO'
    assert if_N(4,-6) == 'NO'

def test_number():
    assert if_N(4,-4) == 1
    assert if_N(2,-2) == 1
    assert if_N(1,1) == -1