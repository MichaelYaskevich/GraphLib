import bisect
import math


def visit(current_node, visited, graph, dist, previous, sorted_nodes):
    visited.add(current_node)
    for neighbor in graph[current_node]:
        if neighbor not in visited:
            update_distance(current_node, neighbor,
                            graph.edge_weight((current_node, neighbor)),
                            dist, previous, sorted_nodes)


def update_distance(current_node, neighbor, weight, dist, previous, sorted_nodes):
    new_dist = dist[current_node] + weight
    if dist[neighbor] > new_dist:
        previous[neighbor] = current_node
        dist[neighbor] = new_dist
        bisect.insort(sorted_nodes,
                      (new_dist, neighbor))


def initialise_distances(nodes, source):
    dist = {}
    for v in nodes:
        dist[v] = math.inf
    dist[source] = 0

    return dist