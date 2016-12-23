import utils as u
import numpy.testing as tst

# generate graph
vertices, adj_list = u.generate_test_graph(100, 0.7, -10, 10)
for v1 in adj_list.keys():
    assert v1 in vertices
    for v2 in adj_list[v1].keys():
        assert v2 in vertices

# generate negative cycle
cycle = u.add_negative_cycle(vertices, adj_list, -10, 10)
for v1 in adj_list.keys():
    assert v1 in vertices
    for v2 in adj_list[v1].keys():
        assert v2 in vertices

# check cycle is really negative
assert u.calculate_cycle_sum(cycle, adj_list) < 0

# save graph to file
u.save_graph_to_file(vertices, adj_list, "1.graph")

# read and check it the same
vertices2, adj_list2 = u.read_graph_from_file("1.graph")
assert len(vertices) == len(vertices2)
for v1 in adj_list.keys():
    for v2 in adj_list[v1].keys():
        tst.assert_approx_equal(adj_list2[v1][v2], adj_list[v1][v2], 2)