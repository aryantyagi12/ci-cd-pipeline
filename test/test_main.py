from src.main import add



def test_add_function():
    assert add(3,4)==7
    assert add(-1,-1)==-2
    assert add(1,0)==1
    assert add(4,6)==10