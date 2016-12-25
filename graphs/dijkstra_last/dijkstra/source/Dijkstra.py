import heapq
from collections import deque, defaultdict
from heapq import *

def dijkstra(graph, initial):
    value_comparison = 0
    value_overhead = 0
    visited = {initial: 0}
    value_overhead += 1
    path = {}
    value_overhead += 1
    nodes = set(graph.nodes)
    value_overhead += 1
    while nodes:
        value_overhead += 1
        min_node = None
        for node in nodes:
            value_overhead += 1
            if node in visited:
                value_overhead += 1
                if min_node is None:
                    value_comparison += 1
                    value_overhead += 1
                    min_node = node
                elif visited[node] < visited[min_node]:
                    value_comparison += 1
                    min_node = node
                    value_overhead += 1
        value_overhead += 1
        if min_node is None:
            break
        value_comparison += 1
        nodes.remove(min_node)
        value_overhead += 1
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            value_comparison+= 1
            try:
                value_overhead += 1
                weight = current_weight + graph.weights[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                value_comparison += 2
                value_overhead += 2
                visited[edge] = weight
                path[edge] = min_node
    return (visited, path, value_comparison, value_overhead)

def shortest_path(graph, dijkstra_output ,initial, destination):
    if len(graph.nodes) <= 1 or initial not in graph.nodes or destination not in graph.nodes:
        return "There is no sense in your request!"
    else:

        visited, paths = dijkstra_output
        print paths
        full_path = deque()
        _destination = paths[destination]
        while _destination != initial:
            full_path.appendleft(_destination)
            _destination = paths[_destination]

        full_path.appendleft(initial)
        full_path.append(destination)

        return visited[destination], list(full_path)

def dijkstra_with_heap(graph, initial, t):
    edges = zip(graph.weights.keys(), graph.weights.values())


    remake_edges = defaultdict(list)
    for direction, weight  in edges:
        remake_edges[direction[0]].append((weight, direction[1]))

    q = [(0, initial, ())]
    visited = set()
    while q:
        (weight, from_node, to_node) = heappop(q)
        if weight not in visited:
            visited.add(from_node)
            to_node = (from_node, to_node)
            if from_node == t: return (weight, [j for j in reversed([i for i in str(to_node).split('\'') if i.isalpha()])] )#[i for i in reversed(to_node)])

            for c, v2 in remake_edges.get(from_node, ()):
                if v2 not in visited:
                    heappush(q, (weight + c, v2, to_node))


    return float("inf")

def dijkstra_with_heap_base(graph, initial):
    visited = []
    heappush(visited, (0, initial))
    path = {}
    visited_result = []
    nodes = set(graph.nodes)
    while nodes:
        min_node = heappop(visited)
        if min_node[1] not in nodes:
            min_node = heappop(visited)
        if min_node is None:
            break

        nodes.remove(min_node[1])

        current_weight = min_node[0]

        for edge in graph.edges[min_node[1]]:
            try:
                weight = current_weight + graph.weights[(min_node[1], edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                heappush(visited,(weight, edge))
                path[edge] = min_node[1]
        visited_result.append(min_node)

    return visited_result, path



