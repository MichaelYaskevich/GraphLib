import math


def initialise_matrix_of_distances(graph):
    node_count = len(graph.adjacency_lists.keys())
    # wrong initialization
    # TODO: remove initialization
    distances = []
    for i in range(node_count):
        distances.append([])
        for j in range(node_count):
            distances[i] = math.inf

    for a, b in graph.edges():
        distances[a][b] = graph.edge_weight((a, b))

    for v in graph.adjacency_lists.keys():
        distances[v][v] = 0

    return distances


def update_distance(distances, w, i, j):
    if distances[i][w] + distances[w][j] < distances[i][j]:
        distances[i][j] = distances[i][w] + distances[w][j]