import math

from GraphLib.dataStructures.di_graph import DiGraph


def floyd_shortest_path(_graph: DiGraph):
    """
     This algorithm finds shortest paths in a directed weighted graph with positive or negative edge weights

    :param _graph: DiGraph
    :return: matrix of distances
    """

    def initialise_matrix_of_distances():
        nonlocal distances

        distances = [[math.inf] * node_count] * node_count
        for a, b in graph.edges():
            distances[a][b] = graph.edge_weight((a, b))

        for v in graph.adjacency_lists.keys():
            distances[v][v] = 0

    def update_distance(_w, _i, _j):
        if distances[_i][_w] + distances[_w][_j] < distances[_i][_j]:
            distances[_i][_j] = distances[_i][_w] + distances[_w][_j]

    distances = []
    graph = _graph
    node_count = len(graph.adjacency_lists.keys())

    initialise_matrix_of_distances()

    for w in range(node_count):
        for i in range(node_count):
            for j in range(node_count):
                update_distance(w, i, j)

    return distances
