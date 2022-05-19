from GraphLib.dataStructures.di_graph import DiGraph


def floyd_shortest_path(graph: DiGraph):
    """
     This algorithm finds shortest paths in a directed weighted graph with positive or negative edge weights

    :param graph: DiGraph
    :return: matrix of distances
    """
    from GraphLib.algorithms.pathSearch.floyd_help_functions import \
        initialise_matrix_of_distances, update_distance

    distances = initialise_matrix_of_distances(graph)

    for w in graph.get_nodes():
        for i in graph.get_nodes():
            for j in graph.get_nodes():
                update_distance(distances, w, i, j)

    return distances
