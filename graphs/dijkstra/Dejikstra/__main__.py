import Graph
from Dijkstra import shortest_path, dijkstra, dijkstra_with_heap
from heapq import *
from collections import defaultdict
from make_data_in_graph import make_data_in_graph


if __name__ == '__main__':
    my_graph = make_data_in_graph('usa_route.txt')
    print dijkstra_with_heap(my_graph, 266, 1151)
    print shortest_path(my_graph, 266, 1151)
    # print dijkstra_with_heap(my_graph, 727, 5414)


    #== shortest_path(my_graph, 727, 730)
    # graph = Graph.Graph()
    #
    # for node in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    #     graph.add_node(node)
    #
    # graph.add_edge('A', 'B', 10)
    # graph.add_edge('A', 'C', 20)
    # graph.add_edge('B', 'D', 15)
    # graph.add_edge('C', 'D', 30)
    # graph.add_edge('B', 'E', 50)
    # graph.add_edge('D', 'E', 30)
    # graph.add_edge('E', 'F', 5)
    # graph.add_edge('F', 'G', 2)
    #
    # print graph.weights
    # print graph.edges
    # print graph.nodes
    # print(shortest_path(graph, 'A', 'G')) # output: (25, ['A', 'B', 'D'])
    # print dijkstra_with_heap(graph, 'B', 'C')
    # print(shortest_path(graph, 'A', 'D'))
    # print graph.edges
    # print dijkstra
    # print dijkstra_with_heap(graph,'A','G' )
    # print(dijkstra_with_heap(graph, 'A', 'D'))
    # visited = []
    # heappush(visited, (0, 'A'))
    # heappush(visited, (6, 'B'))
    # heappush(visited, (48, 'C'))
    # heappush(visited, (-48, 'N'))
    #
    # print heappop(visited)
    # print heappop(visited)
    # print heappop(visited)
    # print heappop(visited)
    #





