import utils as u
from negative_cycle import bellman_ford

# generate graph with negative cycle
vertices, adj_list = u.generate_test_graph(100, 0.7, -10, 10)
cycle = u.add_negative_cycle(vertices, adj_list, -10, 10)

# check bellman ford implementation positive case (with cycles)
cycle2, time_stats = bellman_ford(vertices, adj_list)
assert cycle2 is not None
assert u.calculate_cycle_sum(cycle2, adj_list) < 0
u.save_time_stats("bf_ts_1.txt", time_stats)

# check bellman ford negative case (without cycles)
vertices, adj_list = u.generate_test_graph(100, 0.7, 0.1, 10)
cycle, time_stats = bellman_ford(vertices, adj_list)
assert cycle is None
u.save_time_stats("bf_ts_2.txt", time_stats)