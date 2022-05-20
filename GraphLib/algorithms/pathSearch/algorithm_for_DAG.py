import math

from GraphLib.dataStructures.di_graph import DiGraph
from GraphLib.dataStructures.exception import CycleError


def shortest_paths_for_dag(graph: DiGraph, source: int) -> (dict, dict):
    """
    Finds shortest paths in directed acyclic graph (DAG)
    from source vertex to all other nodes.

    Graph can have edges with negative weights.

    :raises CycleError if there are negative cycles in graph
    :param graph: Digraph
    :param source: first vertex in path
    :return: shortest path tree with distances
    """

    sorted_vertexes = topological_sort(graph.adjacency_lists)

    return find_shortest_paths(sorted_vertexes, graph, source)


def topological_sort(adjacency_lists):
    """
    Sort vertexes in topological order

    :param adjacency_lists: dictionary with vertexes as keys and lists of adjacent vertexes as values
    :return: vertexes in topological order
    :raises CycleError if graph contains cycle
    """
    from GraphLib.algorithms.pathSearch.algorithm_for_DAG_help_methods import \
        initialize_input_degrees, initialize_queue, visit

    deg_in = initialize_input_degrees(adjacency_lists)
    visited = initialize_queue(deg_in, adjacency_lists.keys())
    sorted = []

    while visited.qsize() != 0:
        v = visited.get()
        sorted.append(v)
        for w in adjacency_lists[v]:
            visit(deg_in, w, visited)

    if len(sorted) == len(adjacency_lists.keys()):
        return sorted
    # TODO: выводить цикл, например, найденный через bfs
    raise CycleError("There is a cycle")


def find_shortest_paths(sorted_vertexes: list, graph: DiGraph, source: int) -> (dict, dict):
    """
    Finds shortest paths from source vertex to all other nodes.

    :param sorted_vertexes: vertexes in topological order
    :param graph: Digraph
    :param source: first vertex in path
    :return: shortest path tree with distances
    """
    from GraphLib.algorithms.pathSearch.algorithm_for_DAG_help_methods import \
        find_vertex_index, update_distances

    nodes_count = len(graph.adjacency_lists.keys())
    dist = {}
    for v in graph.get_nodes():
        dist[v] = math.inf
    dist[source] = 0
    prev = {source: None}

    source_index = find_vertex_index(sorted_vertexes, source)

    for k in range(source_index, nodes_count):
        vk = sorted_vertexes[k]
        update_distances(graph, dist, prev, vk)

    return prev, dist
