from rehearsal.if_AB import if_AB

def test_1():
    assert if_AB(1) == '1 bochka'
    assert if_AB(101) == '101 bochka'
    assert if_AB(301) == '301 bochka'

def test_many():
    assert if_AB(10) == '10 bochek'
    assert if_AB(1000) == '1000 bochek'
    assert if_AB(8) == '8 bochek'

def test_some():
    assert if_AB(3) == '3 bochki'
    assert if_AB(4) == '4 bochki'
    assert if_AB(2) == '2 bochki'
    assert if_AB(93) == '93 bochki'
    assert if_AB(194) == '194 bochki'
    assert if_AB(402) == '402 bochki'

def test_exeption():
    assert if_AB(11) == '11 bochek'
    assert if_AB(12) == '12 bochek'
    assert if_AB(13) == '13 bochek'
    assert if_AB(113) == '113 bochek'
    assert if_AB(214) == '214 bochek'