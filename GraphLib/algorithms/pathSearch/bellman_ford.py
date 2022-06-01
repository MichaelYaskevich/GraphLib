from GraphLib.dataStructures.di_graph import DiGraph


def find_shortest_paths(graph: DiGraph, source):
    """
    Finds shortest paths from source vertex to all other nodes.

    Graph can have edges with negative weights.

    :raises NegativeCycleError if there are negative cycles in graph

    :param graph: Digraph
    :param source: first vertex in path
    :return: shortest paths with distances
    """
    from GraphLib.algorithms.pathSearch.path_search_help_functions import get_paths_from_source_to_all
    from GraphLib.algorithms.pathSearch.bellman_ford_help_functions import get_prev_and_dist

    source = str(source)
    prev, dist = get_prev_and_dist(graph, source)
    return get_paths_from_source_to_all(source, prev, dist)


def find_shortest_path(graph: DiGraph, source, destination):
    from GraphLib.algorithms.pathSearch.path_search_help_functions import get_path
    from GraphLib.algorithms.pathSearch.bellman_ford_help_functions import get_prev_and_dist

    source, destination = str(source), str(destination)
    prev, dist = get_prev_and_dist(graph, source)
    return get_path(source, destination, prev), dist[destination]
