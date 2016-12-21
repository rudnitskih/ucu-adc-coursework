from random import uniform, randint


def generate_test_graph(n, connectivity, min_weight, max_weight):
    vertices = range(n)
    adj_list = {}
    for v1 in vertices:
        for v2 in vertices:
            if uniform(0, 1) <= connectivity:
                weight = uniform(min_weight, max_weight)
                set_connection(adj_list, str(v1), str(v2), weight)
    return vertices, adj_list


def set_connection(adj_list, v1, v2, weight):
    if v1 not in adj_list:
        adj_list[v1] = {}
    adj_list[v1][v2] = weight


def has_connection(adj_list, v1, v2):
    if v1 not in adj_list:
        return False
    return v2 in adj_list[v1]


def add_negative_cycle(vertices, adj_list, min_weight, max_weight):
    n = len(vertices)

    # select k random vertices
    k = randint(0, n / 4)
    cycle = []
    for i in range(k):
        random_vertice = str(randint(0, n))
        while random_vertice in cycle:
            random_vertice = str(randint(0, n))

        cycle.append(random_vertice)
    edges_cycle = []

    # check if they have cycle and add edges if needed
    for i in range(len(cycle) - 1):
        v1 = cycle[i]
        v2 = cycle[i + 1]
        if not has_connection(adj_list, v1, v2):
            set_connection(adj_list, v1, v2, uniform(min_weight, max_weight))
        edges_cycle.append(adj_list[v1][v2])

    # calculate weight sum and set last edge so that whole cycle will be negative
    cycle_sum = sum(edges_cycle)
    last_edge_weight = uniform(-cycle_sum - 10, -cycle_sum - 1)
    set_connection(adj_list, cycle[-1], cycle[0], last_edge_weight)
    return cycle


def save_graph_to_file(vertices, adj_list, file_name):
    with open(file_name, "w") as f:
        n = len(vertices)
        f.write(str(n) + "\n")
        for v in vertices:
            f.write(str(v) + "\n")

        for v1, adjacency in adj_list.items():
            f.write("%s" % str(v1))
            for v2, weight in adjacency.items():
                f.write("\t%s %f" % (str(v2), weight))
            f.write("\n")


def read_graph_from_file(file_name):
    with open(file_name, "r") as f:
        n = int(f.readline());
        vertices = []
        for i in range(n):
            vertices.append(f.readline())

        adj_list = {}
        for line in f:
            adjacency = line.split("\t")
            v1 = adjacency[0]
            adj_list[v1] = {}
            for i in range(1,len(adjacency)):
                pair = adjacency[i].split(" ")
                v2 = pair[0]
                weight = float(pair[1])
                adj_list[v1][v2]=weight
        return vertices, adj_list


def to_edges(adj_dictionary):
    for v1 in adj_dictionary.keys():
        for v2 in adj_dictionary[v1].keys():
            yield (v1, v2, adj_dictionary[v1][v2])