import queue

from GraphLib.algorithms.pathSearch.bellman_ford_help_functions \
    import build_cycle
from GraphLib.dataStructures.di_graph import DiGraph
from GraphLib.dataStructures.exception import CycleError


def find_shortest_paths(graph: DiGraph, source):
    """
    Finds shortest paths in directed acyclic graph (DAG)
        from source vertex to all other nodes.

    Graph can have edges with negative weights.

    :raises CycleError if there are negative cycles in graph
    :param graph: Digraph
    :param source: first vertex in path
    :return: shortest path tree with distances
    """

    from GraphLib.algorithms.pathSearch.path_search_help_functions \
        import get_paths_from_source_to_all
    from GraphLib.algorithms.pathSearch.algorithm_for_DAG_help_methods \
        import get_prev_and_dist

    source = str(source)
    prev, dist = get_prev_and_dist(graph, source)
    return get_paths_from_source_to_all(source, prev, dist)


def topological_sort(adjacency_lists):
    """
    Sort vertexes in topological order

    :param adjacency_lists: dictionary with vertexes as keys
        and lists of adjacent vertexes as values
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

    message = '-'.join(get_cycle(adjacency_lists))
    raise CycleError(f"There is a cycle {message}")


def get_cycle(adjacency_lists):
    """
    Finds cycle in graph
    :param adjacency_lists: representation of graph
    :return: cycle as list of nodes or None
    """
    prev = {}
    if len(adjacency_lists) < 2:
        return None
    q = queue.Queue()
    visited = {}
    for node in adjacency_lists.keys():
        if q.qsize() == 0:
            q.put(node)
            visited[node] = True
        else:
            visited[node] = False
    while q.qsize() != 0:
        node = q.get()
        for child in adjacency_lists[node]:
            prev[child] = node
            if visited[child]:
                return build_cycle(node, child, prev)
            else:
                q.put(child)
                visited[child] = True
    return None


def find_shortest_path(graph: DiGraph, source, destination):
    from GraphLib.algorithms.pathSearch.path_search_help_functions \
        import get_path
    from GraphLib.algorithms.pathSearch.algorithm_for_DAG_help_methods \
        import get_prev_and_dist

    source, destination = str(source), str(destination)
    prev, dist = get_prev_and_dist(graph, source)
    return get_path(source, destination, prev), dist[destination]
