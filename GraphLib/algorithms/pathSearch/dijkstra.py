import bisect
import math


def dijkstra_shortest_path(graph, source):
    '''
    Finds shortest paths from source vertex to all other nodes
    :param graph: graph with positive or zero weights
    :param source: first vertex in path
    :return: shortest path tree with distances
    '''

    dist = initialise_distances(graph, source)
    previous = {source: None}
    sorted_nodes = [(source, 0)]
    visited = set()

    run_algorithm_loop(visited, graph, dist, previous, sorted_nodes)

    return previous, dist


def run_algorithm_loop(visited, graph, dist, previous, sorted_nodes):
    while len(sorted_nodes) > 0:
        current_node = sorted_nodes.pop(0)

        if current_node[0] not in visited:
            visit(visited, current_node, graph,
                  dist, previous, sorted_nodes)


def visit(visited, current_node, graph, dist, previous, sorted_nodes):
    node = current_node[0]
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            update(neighbor, current_node, graph,
                   dist, previous, sorted_nodes)


def update(vertex, current_node, graph, dist, previous, sorted_nodes):
    node, distance = current_node
    weight = graph.edge_weight((node, vertex))
    new_dist = distance + weight
    if dist[vertex] > new_dist:
        previous[vertex] = node
        dist[vertex] = new_dist
        bisect.insort(sorted_nodes,
                      (vertex, new_dist))


def initialise_distances(graph, source):
    dist = {}
    for v in graph.adjacency_lists.keys():
        dist[v] = math.inf
    dist[source] = 0
    return dist
