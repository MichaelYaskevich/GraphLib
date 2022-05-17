import bisect
import math


def dijkstra_shortest_path(_graph, source):
    '''
    Finds shortest paths from source vertex to all other nodes
    :param graph: graph with positive or zero weights
    :param source: first vertex in path
    :return: shortest path tree with distances
    '''
    from GraphLib.dataStructures import graph

    dist = {}
    previous = {}
    sorted_nodes = []
    visited = set()
    graph: graph

    def set_up(_graph, source):
        nonlocal graph
        graph = _graph
        initialise_distances(source)
        previous[source] = None
        sorted_nodes.append((source, 0))

    def run_algorithm_loop():
        while len(sorted_nodes) > 0:
            current_node = sorted_nodes.pop(0)

            if current_node[0] not in visited:
                visit(current_node)

    def visit(current_node):
        node = current_node[0]
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                update_distance(current_node, neighbor)

    def update_distance(current_node, neighbor):
        node, distance = current_node
        weight = graph.edge_weight((node, neighbor))
        new_dist = distance + weight
        if dist[neighbor] > new_dist:
            previous[neighbor] = node
            dist[neighbor] = new_dist
            bisect.insort(sorted_nodes,
                          (neighbor, new_dist))

    def initialise_distances(source):
        for v in graph.adjacency_lists.keys():
            dist[v] = math.inf
        dist[source] = 0

    set_up(_graph, source)

    run_algorithm_loop()

    return previous, dist

