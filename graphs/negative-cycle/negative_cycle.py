import numpy as np
def bellman_ford(vertices, edges):
    distance = {}

    for v in vertices:
        distance[v] = np.infty

