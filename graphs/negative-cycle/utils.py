from random import uniform, randint


def generate_test_graph(n, connectivity, min_weight, max_weight):
    edges = {}
    vertices = range(n)
    for v1 in range(n):
        for v2 in range(v1, n):
            if uniform(0, 1) <= connectivity:
                weight = uniform(min_weight, max_weight)
                key = gr_key(v1, v2);
                edges[key] = (v1, v2, weight)
    return vertices, edges


def add_negative_cycle(vertices, edges):
    n = len(vertices)

    # select k random vertices
    k = randint(0, n/4)
    cycle = []
    for i in range(k):
        random_vertice = randint(0, n)
        while random_vertice in cycle:
            random_vertice = randint(0, n)

        cycle.append(random_vertice)
    edges_cycle = []

    # check if they have cycle and add edges if needed
    for i in range(len(cycle)-1):
        v1 = cycle[i]
        v2 = cycle[i+1]
        key = gr_key(v1, v2);
        if not key in edges:
            edges[key] = (v1,v2,uniform(-10, 10))
        edges_cycle.append(edges[key][2])

    # calculate weight sum and set last edge so that whole cycle will be negative
    cycle_sum = sum(edges_cycle)
    last_edge_weight = uniform(-cycle_sum-10, -cycle_sum-1)
    last_edge_key = gr_key(cycle[-1], cycle[0])
    edges[last_edge_key] = (cycle[-1], cycle[0], last_edge_weight)
    return cycle


def save_graph_to_file(vertices, edges, file_name):
    with open(file_name, "w") as f:
        n = len(vertices)
        f.write(str(n) + "\n")
        for v in vertices:
            f.write(str(v) + "\n")

        for key, v in edges.items():
            f.write("%d %d %f\n" % (v[0], v[1], v[2]))


def read_graph_from_file(file_name):
    with open(file_name, "r") as f:
        n = int(f.readline());
        vertices = []
        for i in range(n):
            vertices.append(f.readline())

        edges = {}
        for line in f:
            v = line.split(" ")
            v1 = int(v[0])
            v2 = int(v[1])
            weight = float(v[2])
            edges[gr_key(v[0], v[1])] = (v1,v2,weight)
        return vertices, edges


def gr_key(v1, v2):
    return str(v1) + "_" + str(v2)

