from GraphLib.dataStructures.di_graph import DiGraph


def floyd_shortest_path(graph: DiGraph):
    """
     This algorithm finds shortest paths in a directed weighted graph with positive or negative edge weights

    :param graph: DiGraph
    :return: matrix of distances
    """
    from GraphLib.algorithms.pathSearch.floyd_help_functions import \
        initialise_matrix_of_distances, update_distance

    node_count = len(graph.adjacency_lists.keys())

    distances = initialise_matrix_of_distances(graph)

    for w in range(node_count):
        for i in range(node_count):
            for j in range(node_count):
                update_distance(distances, w, i, j)

    return distances
