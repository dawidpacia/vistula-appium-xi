from math import floor


def calculate_fuel(mass):
    if type(mass) in [int, float] and mass > 0:
        if mass < 9:
            return 1
        else:
            fuel = mass // 3 - 2
            return fuel
    else:
        return False


def calculate_fuel_math_floor(mass):
    fuel = floor(mass / 3) - 2
    return fuel


print(calculate_fuel(1969))
print(calculate_fuel_math_floor(1969))
