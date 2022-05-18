import math

from GraphLib.dataStructures.exception import NegativeCycleError


def find_negative_cycle(graph, dist, previous):
    for w, v in get_better_edges(graph, dist):
        raise_error(w, v, previous)


def update_distances(graph, dist, previous):
    for w, v in get_better_edges(graph, dist):
        update_dist(w, v, dist,
                    graph.edge_weight((w, v)),
                    previous)


def update_dist(prev, current, dist, weight, previous):
    dist[current] = dist[prev] + weight
    previous[current] = prev


def get_better_edges(graph, dist):
    for w, v in graph.edges():
        if dist[w] + graph.edge_weight((w, v)) < dist[v]:
            yield w, v


def raise_error(prev, source, previous):
    message = '-'.join(build_cycle(prev, source, previous))
    raise NegativeCycleError(f"Negative cycle was found {message}")


def build_cycle(prev, source, previous):
    path = [source, prev]
    current = prev
    while current != source:
        current = previous[current]
        path.append(current)

    path.reverse()
    return path


def initialise_distances(nodes, source):
    dist = {}
    for v in nodes:
        dist[v] = math.inf
    dist[source] = 0

    return dist