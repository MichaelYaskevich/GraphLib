import math

from GraphLib.dataStructures.di_graph import DiGraph


def initialise_matrix_of_distances(graph: DiGraph):
    distances = {}
    for i in graph.get_nodes():
        distances[i] = ({})
        for j in graph.get_nodes():
            distances[i][j] = math.inf

    for e in graph.get_edges():
        a, b = e
        distances[a][b] = e.weight

    for v in graph.get_nodes():
        distances[v][v] = 0

    return distances


def update_distance(distances, w, i, j):
    if distances[i][w] + distances[w][j] < distances[i][j]:
        distances[i][j] = distances[i][w] + distances[w][j]