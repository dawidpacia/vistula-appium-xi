for i in range(10):
    print(i)

for i in range(1, 11, 2):
    print(i)

fruits = ("apple", "banana", "cherry")

for fruit in fruits:
    print(fruit)

distances = {
    "Krakow_Nicosia": 1980,
    "Krakow_Reykjavik": 2900,
    "Krakow_Chartum": None
}

for city, distance in distances.items():
    print(city, distance)
