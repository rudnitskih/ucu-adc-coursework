import numpy as np
import time
import utils as u

def bellman_ford(vertices, adj_dictionary):
    #op = [0, 0, 0]
    t_points = {}
    n = len(vertices)
    #op[2] += 1
    s = time.clock()
    distance = dict((v, np.infty) for v in vertices)
    s = u.time_point(s, t_points, "Distance initialization")
    #op[2] += n
    predecessor = dict((v, None) for v in vertices)
    #op[2] += n
    s = u.time_point(s, t_points, "Predecessor initialization")

    while True:
        #op[2] += 1
        s = u.time_point(s, t_points, "While loop iteration start")
        n = len(vertices)
        #op[2] += 1

        # start from first vertice as we don't care about actual path
        v0 = next(iter(vertices))
        #op[2] += 2
        distance[v0] = 0
        #op[2] += 1
        s = u.time_point(s, t_points, "Distance start initialization")

        for i in range(n):
            s = u.time_point(s, t_points, "For loop iteration start")
            #op[2] += 1
            # introduce counter to stop when no changes done
            changes = 0
            #op[2] += 1
            s = u.time_point(s, t_points, "Variable set")

            for v1 in adj_dictionary.keys():
                s = u.time_point(s, t_points, "For loop iteration start")
                #op[2] += 1
                for v2, weight in adj_dictionary[v1].items():
                    s = u.time_point(s, t_points, "For loop iteration start")
                    #op[2] += 1
                    distance_v1 = distance[v1]
                    s = u.time_point(s, t_points, "Dictionary value getting")
                    distance_v1_w = distance_v1 + weight
                    #op[2] += 1
                    s = u.time_point(s, t_points, "Adding")

                    #op[0] += 1
                    if distance_v1_w < distance[v2]:
                        s = u.time_point(s, t_points, "Comparsion")
                        distance[v2] = distance_v1_w
                        s = u.time_point(s, t_points, "Dictionary value setting")
                        #op[1] += 1
                        predecessor[v2] = v1
                        s = u.time_point(s, t_points, "Dictionary value setting")
                        #op[1] += 1
                        changes += 1
                        s = u.time_point(s, t_points, "Adding")
                        #op[2] += 1
            # early stop if all distances processed
            #op[0] += 1
            if changes == 0:
                s = u.time_point(s, t_points, "Comparsion")
                #op[2] += 1
                break
        s = u.time_point(s, t_points, "Ending loop")

        for v1 in adj_dictionary.keys():
            s = u.time_point(s, t_points, "For loop iteration start")
            #op[2] += 1
            for v2, weight in adj_dictionary[v1].items():
                s = u.time_point(s, t_points, "For loop iteration start")
                #op[2] += 1
                #op[0] += 1
                if distance[v1] + weight < distance[v2]:
                    s = u.time_point(s, t_points, "Comparsion")
                    #op[2] += 1
                    # negative cycle found
                    cycle = []
                    s = u.time_point(s, t_points, "Variable set")
                    #op[2] += 1
                    current_vertice = v2
                    s = u.time_point(s, t_points, "Variable set")
                    #op[1] += 1

                    #op[0] += 1
                    while predecessor[current_vertice] != v2:
                        s = u.time_point(s, t_points, "Comparsion")
                        #op[0] += 1
                        prev = predecessor[current_vertice]
                        s = u.time_point(s, t_points, "Dictionary value getting")
                        #op[1] += 1
                        cycle.append(prev)
                        s = u.time_point(s, t_points, "List append")
                        #op[2] += 1
                        current_vertice = prev
                        s = u.time_point(s, t_points, "Variable set")
                        #op[1] += 1

                    return cycle, t_points#op

        # when no cycles found, check if there any vertices with distance infinity
        vertices = {k for k, v in distance.items() if v == np.infty}
        s = u.time_point(s, t_points, "Vertices filtering")
        #op[0] += n
        #op[2] += n

        #op[0] += 1
        if len(vertices) == 0:
            s = u.time_point(s, t_points, "Comparsion")
            #op[2] += 1
            # if no, stop cycle
            break

        # if yes, then run algorithm on that vertices
        adj_len = len(adj_dictionary)
        #op[2] += 1
        adj_dictionary = {k: v for k, v in adj_dictionary.items() if k in vertices}
        s = u.time_point(s, t_points, "Adj filtering")
        #op[0] += adj_len
        #op[2] += adj_len

    return None, t_points#op


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




