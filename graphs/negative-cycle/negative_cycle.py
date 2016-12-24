import numpy as np


def bellman_ford(n, edges):
    op = [0, 0, 0]

    distance = np.empty(n)
    distance[:] = np.infty
    predecessor = np.empty(n, dtype='int')
    predecessor[:] = -1
    op[2] += 4

    while True:
        # start from random vertice as we don't care about actual path
        distance[edges[0][0]] = 0
        predecessor[edges[0][0]] = edges[0][0]
        op[2] += 2

        for i in range(n):
            # introduce counter to stop when no changes done
            changes = 0
            op[2] += 2
            for v1, v2, weight in edges:
                op[2] += 1

                op[0] += 1
                if distance[v1] + weight < distance[v2]:

                    distance[v2] = distance[v1] + weight
                    predecessor[v2] = v1
                    changes += 1
                    op[2] += 4

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
                current_vertice_predecessor = predecessor[current_vertice]
                cycle = [current_vertice]
                op[2] += 4

                while current_vertice_predecessor not in cycle:
                    cycle.append(current_vertice_predecessor)
                    current_vertice = current_vertice_predecessor
                    current_vertice_predecessor = predecessor[current_vertice]
                    op[2] += 4

                current_vertice_predecessor_index = cycle.index(current_vertice_predecessor)
                cycle = cycle[current_vertice_predecessor_index:]
                cycle[::-1]
                op[2] += 3

                return cycle, op

        # when no cycles found, check if there any vertices with distance infinity (invisible from starting point)
        edges2 = []
        op[2] += 1
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


def floyd_warshall(adj_matrix):
    op = [0, 0, 0]
    # init working structures
    n = adj_matrix.shape[0]
    distance = np.copy(adj_matrix)
    predecessor = np.empty((n, n), dtype='int')
    predecessor[:] = -1
    op[2] += 4

    # initialization
    for v1 in range(n):
        for v2 in range(n):
            weight = adj_matrix[v1, v2]
            op[2] += 1

            op[0] += 1
            if weight != np.infty:
                predecessor[v1, v2] = v1
                op[2] += 1
        distance[v1, v1] = 0
        op[2] += 1

    # next steps
    need_stop = False
    diagonal = -1
    op[2] += 2
    for pitstop in range(n):
        op[2] += 1
        for v1 in range(n):
            op[2] += 1
            for v2 in range(n):

                distance_with_pitstop = distance[v1, pitstop] + distance[pitstop, v2]
                op[2] += 2

                op[0] += 1
                if distance_with_pitstop < distance[v1, v2]:
                    distance[v1, v2] = distance_with_pitstop
                    predecessor[v1, v2] = pitstop
                    op[2] += 2
                    # early stop if diagonal have negative value
                    op[0] += 2
                    if v1 == v2 and distance[v1, v2] < 0:
                        need_stop = True
                        diagonal = v1
                        op[2] += 2
                        break

            if need_stop:
                break
        if need_stop:
            break

    # check the actual negative cycle
    op[0] += 1
    if diagonal != -1:
        current_vertice_index = diagonal
        previous_vertice_index = diagonal
        cycle = [current_vertice_index]
        op[2] += 3
        while predecessor[current_vertice_index, previous_vertice_index] not in cycle:
            previous_vertice_index = current_vertice_index
            current_vertice_index = predecessor[current_vertice_index, previous_vertice_index]
            cycle.append(current_vertice_index)
            op[2] += 4

        return cycle, op

    return None, op




