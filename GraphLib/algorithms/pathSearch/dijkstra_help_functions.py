import bisect
import math


def visit(current_node, visited, graph):
    node = current_node[0]
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            update_distance(current_node, neighbor,
                            graph.edge_weight((node, neighbor)))


def update_distance(current_node, neighbor, weight, dist, previous, sorted_nodes):
    node, distance = current_node
    new_dist = distance + weight
    if dist[neighbor] > new_dist:
        previous[neighbor] = node
        dist[neighbor] = new_dist
        bisect.insort(sorted_nodes,
                      (neighbor, new_dist))


def initialise_distances(nodes, source):
    dist = {}
    for v in nodes:
        dist[v] = math.inf
    dist[source] = 0

    return dist