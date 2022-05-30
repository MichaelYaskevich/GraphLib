from GraphLib.dataStructures.di_graph import DiGraph


def floyd_shortest_paths(graph: DiGraph) -> (dict, dict):
    """
     This algorithm finds shortest paths in a directed weighted graph with positive or negative edge weights

    :param graph: DiGraph
    :return: matrix of distances
    """
    from GraphLib.algorithms.pathSearch.floyd_help_functions import \
        initialise_matrix_of_distances, update_distance, initialise_prior_matrix

    distances = initialise_matrix_of_distances(graph)

    prior_matrix = initialise_prior_matrix(graph)
    for w in graph.get_nodes():
        for i in graph.get_nodes():
            for j in graph.get_nodes():
                update_distance(distances, prior_matrix, w, i, j)

    return distances, prior_matrix


def get_path(source, destination, prior_matrix):
    intermediate_node = prior_matrix[source][destination]
    if intermediate_node == destination:
        if destination == source:
            return [source]
        return [source, destination]
    if intermediate_node is None:
        return None
    path: list = get_path(source, intermediate_node, prior_matrix)[:-1]
    for v in get_path(intermediate_node, destination, prior_matrix):
        path.append(v)
    return path

