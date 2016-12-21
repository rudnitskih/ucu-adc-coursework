import utils as u
import random as rnd

# generate graph
rnd.seed(42)
vertices, adj_list = u.generate_test_graph(100, 0.7, -10, 10)

# generate negative cycle
cycle = u.add_negative_cycle(vertices, adj_list, -10, 10)

# check cycle is really negative
s = 0
for i in range(len(cycle)):
    v1 = cycle[i]
    next_key = i+1;
    if i == len(cycle)-1:
        next_key = 0
    v2 = cycle[next_key]
    weight = adj_list[v1][v2]
    s += weight

assert s < 0

# save graph to file
u.save_graph_to_file(vertices, adj_list, "1.graph")

import numpy.testing as tst
# read and check it the same
vertices2, adj_list2 = u.read_graph_from_file("1.graph")
assert len(vertices) == len(vertices2)
for v1 in adj_list.keys():
    for v2 in adj_list[v1].keys():
        tst.assert_approx_equal(adj_list2[v1][v2], adj_list[v1][v2], 2)