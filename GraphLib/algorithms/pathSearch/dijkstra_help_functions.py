import bisect
import math

from GraphLib.dataStructures.di_graph import DiGraph


def visit(current_node, visited, graph: DiGraph, dist, previous, sorted_nodes):
    visited.add(current_node)
    for neighbor in graph.adjacency_lists[current_node]:
        if neighbor not in visited:
            edge = graph.get_incident_edge(current_node, neighbor)
            update_distance(current_node, neighbor, edge.weight,
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