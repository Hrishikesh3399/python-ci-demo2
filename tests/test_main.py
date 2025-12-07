from app.main import add, subtract

def test_add():
    assert add(5, 7) == 12

def test_subtract():
    assert subtract(10, 3) == 7
