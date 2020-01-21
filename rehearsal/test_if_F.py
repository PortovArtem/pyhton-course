from rehearsal import if_F


def test_first():
    """Тесты, с максимальным первым аргументом."""
    assert if_F.max_3(34, 11, 22) == 34
    assert if_F.max_3(19, 15, 11) == 19
    assert if_F.max_3(68, 32, 68) == 68


def test_second():
    """Тесты, с максимальным вторым аргументом."""
    assert if_F.max_3(12, 34, 5) == 34
    assert if_F.max_3(1, 6, 6) == 6
    assert if_F.max_3(22, 45, 4) == 45


def test_thrid():
    """Тесты, с максимальным третьим значением."""
    assert if_F.max_3(12, 67, 88) == 88
    assert if_F.max_3(22, 13, 44) == 44
    assert if_F.max_3(11, 4, 12) == 12


def test_ravno():
    """Тесты, с равными числами"""
    assert if_F.max_3(1, 1, 1) == 1
    assert if_F.max_3(11, 11, 11) == 11
    assert if_F.max_3(55, 55, 55) == 55
