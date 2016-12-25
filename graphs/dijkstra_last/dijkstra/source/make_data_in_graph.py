import Graph
from numpy import sqrt as sqrt
from collections import defaultdict

def make_data_in_graph(file_name):
    graph = Graph.Graph()
    with open(file_name, 'r') as f:
        number = f.readline().rstrip().split()
        nodes = defaultdict(list)
        edges = []

        for i in xrange(int(number[0])):
            tmp = f.readline().rstrip().split()
            nodes[int(tmp[0])] = [int(tmp[1]), int(tmp[2])]
        f.readline().rstrip().split()
        for i in xrange(int(number[0]), int(number[0]) + int(number[1])):
            a = f.readline().rstrip().split()
            edges.append(a)

    for i in edges:
        graph.add_node(int(i[0]))
        graph.add_node(int(i[1]))
        graph.add_edge(int(i[0]), int(i[1]), sqrt((nodes[int(i[1])][0] - nodes[int(i[0])][0])**2 + (nodes[int(i[1])][1] - nodes[int(i[0])][1])**2))

    return graph