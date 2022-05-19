def dijkstra_shortest_paths(graph, source):
    """
    Finds shortest paths from source vertex to all other nodes
    :param graph: graph with positive or zero weights
    :param source: first vertex in path
    :return: shortest path tree with distances
    """
    from GraphLib.algorithms.pathSearch.dijkstra_help_functions import initialise_distances, visit

    previous = {source: None}
    sorted_nodes = [(0, source)]
    visited = set()
    dist = initialise_distances(
        graph.get_nodes(), source)

    while len(sorted_nodes) > 0:
        current_node = sorted_nodes.pop(0)

        if current_node[1] not in visited:
            visit(current_node[1], visited, graph,
                  dist, previous, sorted_nodes)

    return previous, dist
