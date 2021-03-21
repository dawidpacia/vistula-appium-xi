from revision.function_task import calculate_fuel


def test_12():
    assert calculate_fuel(12) == 2

def test_string():
    assert calculate_fuel("test") == False

def test_float():
    assert calculate_fuel(12.0) == 2

def test_negative_value():
    assert calculate_fuel(-2) == False

def test_zero():
    assert calculate_fuel(0) == False

def test_1():
    assert calculate_fuel(1) == 1

def test_8():
    assert calculate_fuel(8) == 1

def test_9():
    assert calculate_fuel(9) == 1
