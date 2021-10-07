import json

f = open("../determine suitability/suitability.json")
points = f.read()
f.close()

points = json.loads(points)
points = sorted(points, key=lambda x: x["suitability"]["total"])

print(len(points))
chosen = points[-1000:]
print(chosen)

chosen = json.dumps(chosen)
f = open("../determine suitability/new_chargers.json", "w+")
f.write(chosen)
f.close()
