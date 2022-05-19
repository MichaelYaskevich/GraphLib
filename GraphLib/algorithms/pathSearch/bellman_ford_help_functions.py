import math

from GraphLib.dataStructures.di_graph import DiGraph
from GraphLib.dataStructures.exception import NegativeCycleError


def find_negative_cycle(graph, dist, previous):
    for w, v in get_better_edges(graph, dist):
        raise_error(w, v, previous)


def update_distances(graph: DiGraph, dist, previous):
    for w, v in get_better_edges(graph, dist):
        edge = graph.get_incident_edge(w, v)
        update_dist(w, v, dist, edge.weight, previous)


def update_dist(current, neighbor, dist, weight, previous):
    dist[neighbor] = dist[current] + weight
    previous[neighbor] = current


def get_better_edges(graph: DiGraph, dist):
    for w, v in graph.get_edges():
        edge = graph.get_incident_edge(w, v)
        if dist[w] + edge.weight < dist[v]:
            yield w, v


def raise_error(prev, source, previous):
    message = '-'.join(build_cycle(prev, source, previous))
    raise NegativeCycleError(f"Negative cycle was found {message}")


def build_cycle(prev, source, previous):
    path = [source, prev]
    current = prev
    while current != source:
        if current not in previous:
            raise Exception("There isn't enough information to build a cycle")
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