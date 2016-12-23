import utils as u
import numpy.testing as tst

# generate graph
adj_matrix = u.generate_test_graph(100, 0.7, -10, 10)

# test convertation to edges
edges = u.adj_matrix_to_edges(adj_matrix)
for edge in edges:
    assert adj_matrix[edge[0], edge[1]] == edge[2]

# generate negative cycle
cycle = u.add_negative_cycle(adj_matrix, -10, 10)

# check cycle is really negative
assert u.calculate_cycle_sum(cycle, adj_matrix) < 0

# save graph to file
u.save_graph_to_file(adj_matrix, "1.graph")

# read and check it the same
adj_matrix2 = u.read_graph_from_file("1.graph")
assert adj_matrix.shape == adj_matrix2.shape
for v1 in range(adj_matrix.shape[0]):
    for v2 in range(adj_matrix.shape[0]):
        tst.assert_approx_equal(adj_matrix2[v1, v2], adj_matrix[v1, v2], 2)