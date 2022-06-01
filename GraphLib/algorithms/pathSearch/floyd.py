from GraphLib.dataStructures.di_graph import DiGraph


def find_shortest_paths_from_all_to_all(graph: DiGraph):
    """
    This algorithm finds shortest paths in a directed weighted graph
        with positive or negative edge weights

    :param graph: DiGraph
    :return: matrix of distances and matrix of previous
    """

    from GraphLib.algorithms.pathSearch.floyd_help_functions import \
        initialise_matrix_of_distances, \
        update_distance, \
        initialise_prior_matrix

    distances = initialise_matrix_of_distances(graph)

    prior_matrix = initialise_prior_matrix(graph)
    for w in graph.get_nodes():
        for i in graph.get_nodes():
            for j in graph.get_nodes():
                update_distance(distances, prior_matrix, w, i, j)

    return distances, prior_matrix


def find_shortest_paths_from_source(graph: DiGraph, source):
    """
    This algorithm finds shortest paths from source node to all other nodes
         in a directed weighted graph with positive or negative edge weights

    :param graph: DiGraph
    :param source: first node in path
    :return: list of paths
    """

    source = str(source)
    distances, prior_matrix = find_shortest_paths_from_all_to_all(graph)
    for node in graph.get_nodes():
        if node != source:
            yield get_path(source, node, prior_matrix), distances[source][node]


def find_shortest_path(graph: DiGraph, source, destination):
    """
    This algorithm finds shortest path from source node to destination node
    :param source: first node in path
    :param destination: last node in path
    :return: path from source to destination or None and distance
    """
    source, destination = str(source), str(destination)
    dist, prior_matrix = find_shortest_paths_from_all_to_all(graph)
    return get_path(source, destination, prior_matrix), dist[destination]


def get_path(source, destination, prior_matrix):
    """
    This algorithm finds shortest path from source node to destination node
    :param source: first node in path
    :param destination: last node in path
    :param prior_matrix: matrix where information about path is stored
    :return: path from source to destination or None
    """

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
