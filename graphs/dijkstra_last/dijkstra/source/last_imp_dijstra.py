from heapq import *

def lst_dijkstra(graph, initial):
    unvisited = set()
    dist = {}
    prev = {}
    nodes = graph.nodes

    for node in nodes:
        dist[node] = float('inf')
        prev[node] = None
        unvisited.add(node)

    dist[initial] = 0

    while unvisited:
        min_node = sorted(dist.items(), key=lambda x: x[1])[0][0]
        if min_node not in unvisited:
            result = {}
            for i in unvisited:
                result[i] = dist[i]
            min_node = sorted(result.items(), key=lambda x: x[1])[0][0]

        unvisited.remove(min_node)
        node_neigbourghs = graph.edges[min_node]

        for node_neigbourgh in node_neigbourghs:
            tmp = dist[min_node] + graph.weights[(min_node, node_neigbourgh)]
            if tmp < dist[node_neigbourgh]:
                dist[node_neigbourgh] = tmp
                prev[node_neigbourgh] = min_node

    return dist, prev

def lst_dijkstra_with_heap(graph, source):
    value_overhead = 0
    value_comparison = 0
    value_overhead += 1
    dist = {}
    value_overhead += 1
    prev = {}
    value_overhead += 1
    dist[source] = 0
    value_overhead += 1
    unvisited = []
    value_overhead += 1
    nodes = graph.nodes
    value_overhead += 1


    for node in nodes:
        value_overhead += 1
        if node != source:
            value_comparison += 1
            value_overhead += 1
            value_overhead += 1
            dist[node] = float('inf')
            prev[node] = None
        value_overhead += 1
        heappush(unvisited,(dist[node], node))

    while unvisited:
        value_overhead += 1
        min_node = heappop(unvisited)[1]
        for node_neighbours in graph.edges[min_node]:
            value_comparison += 1
            value_overhead += 1
            tmp = dist[min_node] + graph.weights[(min_node, node_neighbours)]
            if tmp < dist[node_neighbours]:
                value_comparison += 1
                value_overhead += 1
                value_overhead += 1
                value_overhead += 1
                dist[node_neighbours] = tmp
                prev[node_neighbours] = min_node
                heappush(unvisited, (dist[node_neighbours], node_neighbours))

    return (dist, prev, value_comparison, value_overhead)















