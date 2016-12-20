import utils as u

# generate graph
vertices, edges = u.generate_test_graph(100, 0.7, -10, 10)

# generate negative cycle
cycle = u.add_negative_cycle(vertices, edges)

# check cycle is really negative
s = 0
for i in range(len(cycle)):
    v1 = cycle[i]
    next_key = i+1;
    if i == len(cycle)-1:
        next_key = 0
    v2 = cycle[next_key]
    weight = edges[u.gr_key(v1, v2)][2]
    s += weight

assert s < 0

# save graph to file
u.save_graph_to_file(vertices, edges, "1.graph")

import numpy.testing as tst
# read and check it the same
vertices2, edges2 = u.read_graph_from_file("1.graph")
assert len(vertices) == len(vertices2)
for key in edges.keys():
    assert edges[key][0] == edges2[key][0]
    assert edges[key][1] == edges2[key][1]
    tst.assert_approx_equal(edges[key][2], edges2[key][2], 4)