from math import floor


def calculate_fuel(mass):
    fuel = mass // 3 - 2
    return fuel


def calculate_fuel_math_floor(mass):
    fuel = floor(mass/3) - 2
    return fuel


print(calculate_fuel(1969))
print(calculate_fuel_math_floor(1969))
