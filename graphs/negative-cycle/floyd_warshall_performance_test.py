import utils as u
import numpy as np
import time
from negative_cycle import floyd_warshall
# prevent multithreading
import mkl
mkl.set_num_threads(1)

NN = 5
errors = 0
# test cases 1
for vertices in range(100, 1100, 100):
    for connectivity in np.arange(0.0, 1.2, 0.2):
        # generate graph with negative cycle
        adj_matrix = u.generate_test_graph(vertices, connectivity, -10, 10)
        # and add more
        for c in range(5):
            u.add_negative_cycle(adj_matrix, -10, 10)
        edges = u.adj_matrix_to_edges(adj_matrix)

        # repeat NN times
        for i in range(NN):
            start = time.time()
            cycle2, op = floyd_warshall(adj_matrix)
            if cycle2 is None:
                errors += 1
            end = time.time()

            u.save_test_result("positive1_floyd_warshall.txt", vertices, len(edges), end - start, op)
        print errors

for vertices in range(800, 900, 100):
    for connectivity in np.arange(0.0, 1.25, 0.25):
        # generate graph without negative cycles
        adj_matrix = u.generate_test_graph(vertices, connectivity, 0.1, 10)

        # and add our negative cycles
        for c in range(5):
            u.add_negative_cycle(adj_matrix, -10, 10)
        edges = u.adj_matrix_to_edges(adj_matrix)

        # repeat NN times
        for i in range(NN):
            start = time.time()
            cycle2, op = floyd_warshall(adj_matrix)
            if cycle2 is None:
                errors += 1
            end = time.time()

            u.save_test_result("positive2_floyd_warshall.txt", vertices, len(edges), end - start, op)
        print errors

for vertices in range(100, 800, 100):
    for connectivity in np.arange(0.0, 1.25, 0.25):
        # check bellman ford negative case (without cycles)
        adj_matrix = u.generate_test_graph(vertices, connectivity, 0.1, 10)
        edges = u.adj_matrix_to_edges(adj_matrix)
        # repeat NN times
        for i in range(NN):
            start = time.time()
            cycle2, op = floyd_warshall(adj_matrix)
            if cycle2 is not None:
                errors += 1
            end = time.time()

            u.save_test_result("negative_floyd_warshall.txt", vertices, len(edges), end - start, op)
        print errors