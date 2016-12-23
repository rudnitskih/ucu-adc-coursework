import utils as u
from negative_cycle import bellman_ford

# generate graph with negative cycle
adj_matrix = u.generate_test_graph(10, 0.7, -10, 10)
cycle = u.add_negative_cycle(adj_matrix, -10, 10)
edges = u.adj_matrix_to_edges(adj_matrix)

# check bellman ford implementation positive case (with cycles)
cycle2, op = bellman_ford(adj_matrix.shape[0], edges)
assert cycle2 is not None
assert u.calculate_cycle_sum(cycle2, adj_matrix) < 0

# check bellman ford negative case (without cycles)
adj_matrix = u.generate_test_graph(10, 0.7, 0.1, 10)
edges = u.adj_matrix_to_edges(adj_matrix)
cycle, op = bellman_ford(adj_matrix.shape[0], edges)
assert cycle is None
