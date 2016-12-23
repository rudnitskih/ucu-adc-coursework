from random import uniform, randint
import time
import numpy as np


def generate_test_graph(n, connectivity, min_weight, max_weight):
    adj_matrix = np.zeros((n, n))
    adj_matrix[:] = np.infty
    for v1 in range(n):
        for v2 in range(n):
            if v1 != v2 and uniform(0, 1) <= connectivity:
                weight = uniform(min_weight, max_weight)
                adj_matrix[v1, v2] = weight
    return adj_matrix


#def get_graph_for_performance_testing(n, m, connectivity, min_weight, max_weight)


def adj_matrix_to_edges(adj_matrix):
    edges = []
    n = adj_matrix.shape[0]
    for v1 in range(n):
        for v2 in range(n):
            if adj_matrix[v1, v2] != np.infty:
                edges.append((v1, v2, adj_matrix[v1,v2]))
    return edges


def add_negative_cycle(adj_matrix, min_weight, max_weight):
    n = adj_matrix.shape[0]

    # select k random vertices
    k = randint(2, n / 4)
    cycle = []
    for i in range(k):
        random_vertice = randint(0, n-1)
        while random_vertice in cycle:
            random_vertice = randint(0, n-1)

        cycle.append(random_vertice)
    edges_cycle = []

    # check if they have cycle and add edges if needed
    for i in range(len(cycle) - 1):
        v1 = cycle[i]
        v2 = cycle[i + 1]
        if adj_matrix[v1, v2] == np.infty:
            adj_matrix[v1, v2] = uniform(min_weight, max_weight)
        edges_cycle.append(adj_matrix[v1, v2])

    # calculate weight sum and set last edge so that whole cycle will be negative
    cycle_sum = sum(edges_cycle)
    last_edge_weight = uniform(-cycle_sum - 10, -cycle_sum - 1)
    adj_matrix[cycle[-1], cycle[0]] = last_edge_weight
    return cycle


def save_graph_to_file(adj_matrix, file_name):
    with open(file_name, "w") as f:
        n = adj_matrix.shape[0]
        f.write("%d\n" % n)
        for v1 in range(n):
            for v2 in range(n):
                f.write("%s " % str(adj_matrix[v1, v2]))
            f.write("\n")


def read_graph_from_file(file_name):
    with open(file_name, "r") as f:
        n = int(f.readline());

        adj_matrix = np.zeros((n, n))
        v1 = 0
        for line in f:
            values = filter(lambda x: x != "\n", line.split(" "))
            for v2 in range(0, len(values)):
                adj_matrix[v1, v2] = float(values[v2])
            v1 += 1
        return adj_matrix


def calculate_cycle_sum(cycle, adj_matrix):
    s = 0
    for i in range(len(cycle)):
        v1 = cycle[i]
        next_key = i+1;
        if(next_key == len(cycle)):
            next_key = 0
        v2 = cycle[next_key]
        weight = adj_matrix[v1, v2]
        s += weight
    return s


def time_point(start, dict, name):
    end = time.time()
    if name in dict:
        dict[name] = (dict[name][0] + end-start, dict[name][1] + 1)
    else:
        dict[name] = (end-start, 1)
    return end


def save_time_stats(file_name, dict):
    with open(file_name, "w") as f:
        for point, (duration, times) in dict.items():
            f.write("%s: %.12f, %d, %.12f\n"%(point, duration, times, duration/times))