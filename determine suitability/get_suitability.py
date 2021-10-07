import json

f = open("../Car Park Data/car_parks.json")
data = f.read()
f.close()
car_parks = json.loads(data)

f = open("../charging points/charging_grid.json")
data = f.read()
f.close()
grid = json.loads(data)

f = open("../net production/net.json")
data = f.read()
f.close()
net = json.loads(data)

net_grid = []

for x in range(655):
    row = []
    for y in range(1211):
        row.append([])

    net_grid.append(row)

for x in net:
    net_grid[x["x"]][x["y"]] = x["kw"]



print(net_grid)

car_parks_suitability = []
for car_park in car_parks:
    x = car_park["x"]//1000
    y = car_park["y"]//1000

    count = grid[x][y]
    print(x)
    print(y)
    print(len(net_grid))
    print(net_grid[x])
    demand = net_grid[x][y]
    car_park_suitability = car_park.copy()
    car_park_suitability["suitability"] = {"count": count, "demand": demand*-1}
    car_parks_suitability.append(car_park_suitability)

data = json.dumps(car_parks_suitability)
f = open("../determine suitability/data.json", "w+")
f.write(data)
f.close()
