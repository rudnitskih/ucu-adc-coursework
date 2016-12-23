import utils as u
from negative_cycle import floyd_warshall

# generate graph with negative cycle
vertices, adj_list = u.generate_test_graph(1000, 0.7, -10, 10)
cycle = u.add_negative_cycle(vertices, adj_list, -10, 10)

# check floyd warshall implementation positive case
cycle3 = floyd_warshall(vertices, adj_list)
assert cycle3 is not None
assert u.calculate_cycle_sum(cycle3, adj_list) < 0

# check floyd warshall negative case (without cycles)
vertices, adj_list = u.generate_test_graph(1000, 0.7, 0.1, 10)
cycle = floyd_warshall(vertices, adj_list)
assert cycle is None