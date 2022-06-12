import math
import queue

from GraphLib.algorithms.pathSearch.algorithm_for_DAG import topological_sort
from GraphLib.dataStructures.di_graph import DiGraph


# TODO: написать doc strings везде
def initialize_input_degrees(adjacency_lists):
    deg_in_dict = {}
    for v in adjacency_lists.keys():
        deg_in_dict[v] = 0

    for vertex in adjacency_lists.keys():
        for neighbor in adjacency_lists[vertex]:
            deg_in_dict[neighbor] += 1

    return deg_in_dict


def initialize_queue(deg_in_list, nodes):
    q = queue.Queue()

    for vertex in nodes:
        if deg_in_list[vertex] == 0:
            q.put(vertex)

    return q


def visit(deg_in_list, vertex, visited_queue):
    deg_in_list[vertex] -= 1
    if deg_in_list[vertex] == 0:
        visited_queue.put(vertex)


def update_distances(graph: DiGraph, distances: dict, previous: dict, vertex):
    for w in graph.adjacency_lists[vertex]:
        edge = graph.get_incident_edge(vertex, w)
        if distances[vertex] + edge.weight < distances[w]:
            distances[w] = distances[vertex] + edge.weight
            previous[w] = vertex


def find_vertex_index(vertexes, vertex):
    index = -1
    for (i, v) in enumerate(vertexes):
        if v == vertex:
            index = i
            break

    return index


def find_shortest_paths(sorted_vertexes: list, graph: DiGraph, source):
    """
    Finds shortest paths from source vertex to all other nodes.

    :param sorted_vertexes: vertexes in topological order
    :param graph: Digraph
    :param source: first vertex in path
    :return: shortest path tree with distances
    """

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


def get_prev_and_dist(graph: DiGraph, source):
    sorted_vertexes = topological_sort(graph.adjacency_lists)

    return find_shortest_paths(sorted_vertexes, graph, source)
