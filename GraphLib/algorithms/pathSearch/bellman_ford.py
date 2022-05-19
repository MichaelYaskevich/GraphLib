from GraphLib.dataStructures.di_graph import DiGraph


def shortest_paths_bellman_ford(graph: DiGraph, source: int) -> (dict, dict):
    '''
    Finds shortest paths from source vertex to all other nodes.

    Graph can have edges with negative weights.

    :raises NegativeCycleError if there are negative cycles in graph

    :param graph: Digraph
    :param source: first vertex in path
        :return: shortest path tree with distances
    '''
    from GraphLib.algorithms.pathSearch.bellman_ford_help_functions import \
        initialise_distances, update_distances, find_negative_cycle

    previous = {source: None}
    dist = initialise_distances(
        graph.adjacency_lists.key(), source)

    for _ in range(1, len(graph.edges())):
        update_distances(graph, dist, previous)

    find_negative_cycle(graph, dist, previous)

    return previous, dist

