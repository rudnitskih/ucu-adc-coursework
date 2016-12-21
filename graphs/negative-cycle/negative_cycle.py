import numpy as np
import random as rnd
def bellman_ford(vertices, edges):
    distance = {}
    n = len(vertices)

    for v in vertices:
        distance[v] = np.infty

    # find first vertice with distance equal to infinity, another words next connectivity component
    distance[0] = 0




