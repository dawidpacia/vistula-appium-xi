route = "Krakow_Reykjavik"

distances = {
"Krakow_Nicosia" : 1980,
"Krakow_Reykjavik": 2900,
"Krakow_Chartum": None
}

distance = distances[route]


if distance < 2000:
    cost = 2 * distance + 100
elif distance >= 2000:
    cost = 2 * distance
else:
    print("Route has no connection")
    cost = False

print(f"Total cost of route {route} is {cost}$")