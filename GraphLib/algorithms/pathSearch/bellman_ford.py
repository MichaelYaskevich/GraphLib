import math

from GraphLib.dataStructures.di_graph import DiGraph
from GraphLib.dataStructures.exception import NegativeCycleError

dist = {}
graph: DiGraph
previous = {}


def shortest_paths_bellman_ford(_graph: DiGraph, source: int) -> (dict, dict):
    '''
    Finds shortest paths from source vertex to all other nodes.

    Graph can have edges with negative weights.

    :raises NegativeCycleError if there are negative cycles in graph

    :param _graph: Digraph
    :param source: first vertex in path
        :return: shortest path tree with distances
    '''

    def set_up(_graph, source):
        global graph
        graph = _graph
        initialise_distances(source)
        previous[source] = None

    def initialise_distances(source):
        for v in graph.adjacency_lists.keys():
            dist[v] = math.inf
        dist[source] = 0

    def update_distances():
        for w, v in get_better_edges():
            update_dist(w, v)

    def update_dist(prev, current):
        dist[current] = dist[prev] + graph.edge_weight((prev, current))
        previous[current] = prev

    def get_better_edges():
        for w, v in graph.edges():
            if dist[w] + graph.edge_weight((w, v)) < dist[v]:
                yield w, v

    def find_negative_cycle():
        for w, v in get_better_edges():
            raise_error(w, v)

    def raise_error(prev, source):
        message = '-'.join(build_cycle(prev, source))
        raise NegativeCycleError(f"Negative cycle was found {message}")

    def build_cycle(prev, source):
        path = [source, prev]
        current = prev
        while current != source:
            current = previous[current]
            path.append(current)

        path.reverse()
        return path

    set_up(source)

    for _ in range(1, len(graph.edges())):
        update_distances()

    find_negative_cycle()

    return previous, dist
