import utils as u
import collections

results = []
with open("_/floyd-warshall.txt", "r") as f:
    for line in f:
        data = line.split("\t")
        vertices = int(data[0])
        edges = int(data[1])
        duration = float(data[2])
        op = int(data[3]) + int(data[5])
        results.append((vertices, edges, duration, op))

results2 = {}
for vertices, edges, duration, op in results:
    if vertices not in results2:
        results2[vertices] = {}
    if edges not in results2[vertices]:
        results2[vertices][edges] = (duration, op, 1)
    else:
        results2[vertices][edges] = (duration + results2[vertices][edges][0], op + results2[vertices][edges][1], 1 + results2[vertices][edges][2])\

for vertices in sorted(results2.keys()):
    c = [0.1, 0.25, 0.5, 0.75, 1.0]
    sorted_edges = sorted(results2[vertices].keys())
    for i in range(5):
        if i < len(sorted_edges):
            edges = sorted_edges[i]
            connectivity = c[i]
            (duration, op, count) = results2[vertices][edges]
            duration = duration/count
            op = op/count

            u.save_test_result2("results/floyd-warshall-%.2f.txt"%connectivity, vertices, duration, op)


