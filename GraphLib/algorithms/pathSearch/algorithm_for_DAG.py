import math
import queue

from GraphLib.dataStructures.di_graph import DiGraph
from GraphLib.dataStructures.exception import CycleError


def shortest_path_for_dag(graph: DiGraph, source):
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

    return find_shortest_path(sorted_vertexes, graph, source)


def topological_sort(adjacency_lists):
    """
    Sort vertexes in topological order

    :param adjacency_lists: dictionary with vertexes as keys and lists of adjacent vertexes as values
    :return: vertexes in topological order
    :raises CycleError if graph contains cycle
    """
    nodes_count = len(adjacency_lists)

    def initialize_input_degrees():
        deg_in_list = [0] * nodes_count

        for vertex in range(nodes_count):
            for neighbor in adjacency_lists[vertex]:
                deg_in_list[neighbor - 1] += 1

        return deg_in_list

    def initialize_queue(deg_in_list):
        q = queue.Queue()

        for vertex in range(nodes_count):
            if deg_in_list[vertex] == 0:
                q.put(vertex)

        return q

    def visit(deg_in_list, vertex, visited_queue):
        deg_in_list[vertex - 1] -= 1
        if deg_in_list[vertex - 1] == 0:
            visited_queue.put(vertex - 1)

    deg_in = initialize_input_degrees()
    visited = initialize_queue(deg_in)
    sorted = []

    while visited.qsize() != 0:
        v = visited.get()
        sorted.append(v)
        for w in adjacency_lists[v]:
            visit(deg_in, w, visited)

    if len(sorted) == len(adjacency_lists.keys()):
        return sorted
    raise CycleError("")


def find_shortest_path(sorted_vertexes: list, graph: DiGraph, source: int):
    """
    Finds shortest paths from source vertex to all other nodes.

    :param sorted_vertexes: vertexes in topological order
    :param graph: Digraph
    :param source: first vertex in path
    :return: shortest path tree with distances
    """

    def update_distances(distances, previous, vertex):
        for w in graph.adjacency_lists[vertex]:
            weight = graph.edge_weight((vertex, w))
            if distances[vertex] + weight < distances[w - 1]:
                distances[w - 1] = distances[vertex] + weight
                previous[w - 1] = vertex

    def find_vertex_index(vertexes, vertex):
        index = -1
        for (i, v) in enumerate(vertexes):
            if v == vertex - 1:
                index = i
                break

        return index

    nodes_count = len(graph.adjacency_lists.keys())
    dist = [math.inf] * nodes_count
    dist[source - 1] = 0
    prev = {source - 1: -1}

    source_index = find_vertex_index(sorted_vertexes, source)

    for k in range(source_index, nodes_count):
        vk = sorted_vertexes[k]
        update_distances(dist, prev, vk)

    return prev, dist
