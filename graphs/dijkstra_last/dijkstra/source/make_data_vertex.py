import Graph
from numpy import sqrt as sqrt
from collections import defaultdict

def make_data_vertex(file_name, number_of_vertex):
    graph = Graph.Graph()

    with open(file_name, 'r') as f:
        number = f.readline().rstrip().split()
        nodes = defaultdict(list)
        edges = []
        what_can = range(number_of_vertex)

        for i in xrange(int(number[0])):
            tmp = f.readline().rstrip().split()
            if int(tmp[0]) in what_can:
                nodes[int(tmp[0])] = [int(tmp[1]), int(tmp[2])]
            else:
                continue
        f.readline()

        for i in xrange(int(number[0]), int(number[0]) + int(number[1])):
            a = f.readline().rstrip().split()
            if int(a[0]) in nodes and int(a[1]) in nodes:
                edges.append(a)
            else:
                continue
        for i in edges:
            graph.add_node(int(i[0]))
            graph.add_node(int(i[1]))
            graph.add_edge(int(i[0]), int(i[1]), sqrt((nodes[int(i[1])][0] - nodes[int(i[0])][0])**2 + (nodes[int(i[1])][1] - nodes[int(i[0])][1])**2))

    return graph





