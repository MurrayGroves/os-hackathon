import json

f = open("../determine suitability/new_chargers.json")
data = f.read()
f.close()
chargers = json.loads(data)

f = open("../charging points/charging_grid.json")
data = f.read()
f.close()
grid = json.loads(data)

for charger in chargers:
    grid[charger["x"]//1000][charger["y"]//1000] += 30  # On average, each charger is 30KW

grid = json.dumps(grid)
f = open("../new chargers/grid.json", "w+")
f.write(grid)
f.close()
