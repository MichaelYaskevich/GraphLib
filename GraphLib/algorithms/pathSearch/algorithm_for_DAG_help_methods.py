import queue

from GraphLib.dataStructures.di_graph import DiGraph


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
