import numpy as np


def bellman_ford(n, edges):
    op = [0, 0, 0]

    distance = np.empty(n)
    op[2] += 1
    distance[:] = np.infty
    op[1] += 1
    predecessor = np.empty(n, dtype='int')
    op[2] += 1
    predecessor[:] = -1
    op[1] += 1

    while True:
        op[2] += 1
        # start from random vertice as we don't care about actual path
        distance[edges[0][0]] = 0
        op[1] += 1
        predecessor[edges[0][0]] = edges[0][0]
        op[1] += 1

        for i in range(n):
            op[2] += 1
            # introduce counter to stop when no changes done
            changes = 0
            op[1] += 1
            for v1, v2, weight in edges:
                op[2] += 1

                op[0] += 1
                if distance[v1] + weight < distance[v2]:

                    distance[v2] = distance[v1] + weight
                    op[1] += 1
                    predecessor[v2] = v1
                    op[1] += 1
                    changes += 1
                    op[1] += 1

            # early stop if all distances processed
            op[0] += 1
            if changes == 0:
                break

        for v1, v2, weight in edges:
            op[2] += 1

            op[0] += 1
            if distance[v1] + weight < distance[v2]:

                # negative cycle found
                current_vertice = v2
                op[1] += 1
                current_vertice_predecessor = predecessor[current_vertice]
                op[1] += 1
                cycle = [current_vertice]
                op[1] += 1

                while current_vertice_predecessor not in cycle:
                    op[2] += 1
                    cycle.append(current_vertice_predecessor)
                    op[2] += 1
                    current_vertice = current_vertice_predecessor
                    op[1] += 1
                    current_vertice_predecessor = predecessor[current_vertice]
                    op[2] += 1

                current_vertice_predecessor_index = cycle.index(current_vertice_predecessor)
                op[2] += 1
                cycle = cycle[current_vertice_predecessor_index:]
                op[2] += 1
                cycle[::-1]
                op[2] += 1

                return cycle, op

        # when no cycles found, check if there any vertices with distance infinity (invisible from starting point)
        edges2 = []
        op[1] += 1
        for edge in edges:
            op[2] += 1

            op[0] += 1
            if distance[edge[0]] == np.infty:
                edges2.append(edge)
                op[2] += 1

        edges = edges2
        op[2] += 1

        op[0] += 1
        # if no invisible vertices
        if len(edges) == 0:
            break
        # if yes run again
        n = 0
        op[1] += 1
        for d in distance:
            op[2] += 1

            op[0] += 1
            if d == np.infty:
                n += 1
                op[2] += 1

    return None, op


def floyd_warshall(vertices, adj_dictionary):
    # init working structures
    n = len(vertices)
    distance = np.empty((n, n))
    predecessor = np.empty((n, n), dtype='string')
    distance[:] = np.infty

    # step 0
    for i in range(n):
        distance[i, i] = 0
        vertice = vertices[i]
        adj = adj_dictionary[vertice]
        for vertice2, weight in adj.items():
            i2 = vertices.index(vertice2)
            distance[i, i2] = weight
            predecessor[i, i2] = vertice2

    # next steps
    for i in range(n):
        pitstop = vertices[i]
        for j1 in range(n):
            for j2 in range(n):
                distance_with_pitstop = distance[j1, i] + distance[i, j2]
                if distance_with_pitstop < distance[j1, j2]:
                    distance[j1, j2] = distance_with_pitstop
                    predecessor[j1, j2] = pitstop

    # check the actual negative cycle
    for i in range(n):
        diagonal_weight = distance[i, i]
        if diagonal_weight < 0:
            # we have a negative cycle! let's trace it back
            current_vertice = vertices[i]
            current_vertice_index = i
            previous_vertice_index = i
            cycle = [current_vertice]
            while predecessor[previous_vertice_index, current_vertice_index] not in cycle:
                current_vertice = predecessor[previous_vertice_index, current_vertice_index]
                previous_vertice_index = current_vertice_index
                current_vertice_index = vertices.index(current_vertice)
                cycle.append(current_vertice)

            return cycle

    return None




