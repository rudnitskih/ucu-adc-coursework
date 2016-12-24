import utils as u
from negative_cycle import floyd_warshall

# generate graph with negative cycle
adj_matrix = u.generate_test_graph(100, 0.7, -10, 10)
cycle = u.add_negative_cycle(adj_matrix, -10, 10)

# check floyd warshall implementation positive case
cycle3, op = floyd_warshall(adj_matrix)
assert cycle3 is not None
assert u.calculate_cycle_sum(cycle3, adj_matrix) < 0

# check floyd warshall negative case (without cycles)
adj_matrix = u.generate_test_graph(100, 0.7, 0.1, 10)
cycle, op = floyd_warshall(adj_matrix)
assert cycle is None