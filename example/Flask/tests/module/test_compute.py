from src.module.compute import Add

def test_compute():
    '''Test computation'''

    assert Add(1, 2) == 3
    assert Add(2, 2) == 4
    assert Add(8, 2) == 10
    assert Add(10, -2) == 8