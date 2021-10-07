import json

import json

f = open("../consumption/consumption.json")
consumption = f.read()
f.close()

f = open("../new chargers/grid.json")
chargers = f.read()
f.close()

consumption, chargers = json.loads(consumption), json.loads(chargers)
net = []
for point in consumption:
    new_point = point.copy()
    x, y = point["x"], point["y"]
    new_point["kw"] = point["kw"] + chargers[x][y]
    net.append(new_point)

f = open("../new chargers/net.json", "w+")
f.write(json.dumps(net))
f.close()

count = 0
for i in net:
    count += i["kw"]

print(f"New Surplus UK charging capacity: {count}")
