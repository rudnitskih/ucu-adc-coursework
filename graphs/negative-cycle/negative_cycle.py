import numpy as np
import utils as u


def bellman_ford(vertices, adj_dictionary):
    distance = {}
    predecessor = {}

    n = len(vertices)

    for v in vertices:
        distance[v] = np.infty
        predecessor[v] = None

    distance[0] = 0

    for i in range(n):
        for v1, v2, weight in u.to_edges(adj_dictionary):
            if(distance[v1] + weight < distance[v2]):
                distance[v2] = distance[v1] + weight
                predecessor[v2] = v1

    for v1, v2, weight in u.to_edges(adj_dictionary):
        if distance[v1] + weight < distance[v2] :
            # negative cycle found
            cycle = []
            current_vertice = v2
            while predecessor[current_vertice] not in cycle:
                prev = predecessor[current_vertice]
                cycle.append(prev)
                current_vertice = prev
            cycle_vertice = predecessor[current_vertice]
            index = cycle.index(cycle_vertice)
            cycle = cycle[index:]
            cycle.append(cycle_vertice)

            return cycle

    # if no cycles check if there are vertices with distance infinity
    invisible_vertices = [k for k, v in distance.items() if v == np.infty]
    if len(invisible_vertices) > 0:
        invisible_adj = {k: v for k, v in adj_dictionary.items() if k in invisible_vertices}
        return bellman_ford(invisible_vertices, invisible_adj)

    return None


