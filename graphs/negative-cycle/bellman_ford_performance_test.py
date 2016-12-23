import utils as u
from negative_cycle import bellman_ford

# generate graph with negative cycle
adj_matrix = u.generate_test_graph(1000, 0.7, -10, 10)
cycle = u.add_negative_cycle(adj_matrix, -10, 10)

# check bellman ford implementation positive case (with cycles)
cycle2 = bellman_ford(adj_matrix)
assert cycle2 is not None
assert u.calculate_cycle_sum(cycle2, adj_matrix) < 0

# check bellman ford negative case (without cycles)
adj_matrix = u.generate_test_graph(1000, 0.7, 0.1, 10)
cycle = bellman_ford(adj_matrix)
assert cycle is None
