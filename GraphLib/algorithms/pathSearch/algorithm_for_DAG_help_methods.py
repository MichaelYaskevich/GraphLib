import queue


def initialize_input_degrees(adjacency_lists):
    nodes_count = len(adjacency_lists.keys())
    deg_in_list = [0] * nodes_count

    for vertex in range(nodes_count):
        for neighbor in adjacency_lists[vertex]:
            deg_in_list[neighbor - 1] += 1

    return deg_in_list


def initialize_queue(deg_in_list, nodes_count):
    q = queue.Queue()

    for vertex in range(nodes_count):
        if deg_in_list[vertex] == 0:
            q.put(vertex)

    return q


def visit(deg_in_list, vertex, visited_queue):
    deg_in_list[vertex - 1] -= 1
    if deg_in_list[vertex - 1] == 0:
        visited_queue.put(vertex - 1)


def update_distances(graph, distances, previous, vertex):
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
