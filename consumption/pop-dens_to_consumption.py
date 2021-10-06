import json

CONSUMPTION = 0.124583333  # KW per person

f = open("population density/data processor/nooffset.json")
data = f.read()
f.close()

data = json.loads(data)

new_data = []
for point in data:
    new_point = point.copy()
    density = new_point["density"] if (new_point["density"] != -9999) else 0
    new_point["kw"] = -1 * CONSUMPTION * density
    new_point.pop("density")
    new_data.append(new_point)

new_data = json.dumps(new_data)
f = open("consumption/consumption.json", "w+")
f.write(new_data)
f.close()
