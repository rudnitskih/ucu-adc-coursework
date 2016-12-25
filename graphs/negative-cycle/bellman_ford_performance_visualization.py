import matplotlib.pyplot as plt
import collections as c

results = []
with open("data/bellman-ford.txt", "r") as f:
    for line in f:
        data = line.split("\t")
        vertices = int(data[0])
        edges = int(data[1])
        duration = float(data[2])
        op = int(data[3]) + int(data[5])
        results.append((vertices, edges, duration, op))

durations = {}
durations_c = {}
ops = {}
for vertices, edges, duration, op in results:
    key = vertices*edges
    if key not in durations:
        durations[key] = 0
        durations_c[key] = 0
    durations[key] += duration
    durations_c[key] += 1
    ops[key] = op

for key, duration in durations.items():
    durations[key] = duration/durations_c[key]

durations_sorted = c.OrderedDict(sorted(durations.items()))
plt.plot(durations_sorted.keys(), durations_sorted.values())
plt.show()
