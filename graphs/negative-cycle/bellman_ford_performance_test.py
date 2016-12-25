import utils as u
import numpy as np
import time
from negative_cycle import bellman_ford
# prevent multithreading
import mkl
mkl.set_num_threads(1)

NN = 5
errors = 0
# test cases 1
for vertices in range(100, 1100, 100):
    for connectivity in np.arange(0.1, 1.2, 0.2):
        # generate graph with negative cycle
        adj_matrix = u.generate_test_graph(vertices, connectivity, -10, 10)
        # and add more
        for c in range(5):
            u.add_negative_cycle(adj_matrix, -10, 10)
        edges = u.adj_matrix_to_edges(adj_matrix)

        start = time.time()
        # repeat NN times
        for i in range(NN):
            cycle2, op = bellman_ford(vertices, edges)
            if cycle2 is None:
                errors += 1
        end = time.time()

        u.save_test_result("results/bellman-ford-%.2f.txt"%connectivity, vertices, (end - start)/NN, op)
        print errors