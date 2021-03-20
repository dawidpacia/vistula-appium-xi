from reviesion.task_calculator import Calculator

calc = Calculator()

def test_add():
    assert calc.sum(1, 2) == 3

def test_division():
    assert calc.divide(1, 2) == 0.5

def test_division_by_zero():
    assert calc.divide(1, 0) == False

def test_multiply():
    assert calc.multiply(-1, -1) == 1
