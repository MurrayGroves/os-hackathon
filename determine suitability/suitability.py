import json


def calculate_suitability(count, demand):
    if demand == []:
        demand = 0
    if count == 0:
        count = 0.1

    suitability = demand/count
    return suitability


f = open("../determine suitability/data.json")
points = f.read()
f.close()
points = json.loads(points)

new_points = []
for point in points:
    suitability = calculate_suitability(point["suitability"]["count"], point["suitability"]["demand"])
    new_point = point.copy()
    new_point["suitability"]["total"] = suitability
    new_points.append(new_point)


new_points = json.dumps(new_points)
f = open("../determine suitability/suitability.json", "w+")
f.write(new_points)
f.close()
