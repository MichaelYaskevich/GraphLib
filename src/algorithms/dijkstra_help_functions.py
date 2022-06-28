import bisect
import math

from src.data_structures.di_graph import DiGraph


def visit(current_node, visited, graph: DiGraph,
          dist, previous, sorted_nodes):
    """
    Посещает вершину и ищет более короткие расстояния.

    :param current_node: дистанция до вершины и вершина как кортеж
    :param visited: множество посещенных вершин
    :param graph: граф
    :param dist: массив расстояний
    :param previous: массив предудущих
    :param sorted_nodes: вершины отсортированные по расстояниям до них
    """

    visited.add(current_node)
    for neighbor in graph.adjacency_lists[current_node]:
        if neighbor not in visited:
            edge = graph.get_incident_edge(current_node, neighbor)
            update_distance(current_node, neighbor, edge.weight,
                            dist, previous, sorted_nodes)


def update_distance(current_node, neighbor,
                    weight, dist, previous, sorted_nodes):
    """
    Посещает вершину и ищет более короткие расстояния.

    :param current_node: дистанция до вершины и вершина как кортеж
    :param neighbor: соседняя вершина
    :param weight: вес ребра между current_node и neighbor
    :param dist: массив расстояний
    :param previous: массив предудущих
    :param sorted_nodes: вершины отсортированные по расстояниям до них
    """

    new_dist = dist[current_node] + weight
    if dist[neighbor] > new_dist:
        previous[neighbor] = current_node
        dist[neighbor] = new_dist
        bisect.insort(sorted_nodes,
                      (new_dist, neighbor))


def initialise_distances(nodes, source: str):
    """
    Создает массив расстояний.

    :param nodes: вершины графа
    :param source: вершина-источник
    :return: массив расстояний
    """

    dist = {}
    for v in nodes:
        dist[v] = math.inf
    dist[source] = 0

    return dist


def get_prev_and_dist(graph: DiGraph, source: str):
    """
    Находит кратчайшие пути от source до всех вершин.

    :param graph: граф
    :param source: вершина-источник
    :return: массив предудущих, массив расстоний
    """

    previous = {source: None}
    sorted_nodes = [(0, source)]
    visited = set()
    dist = initialise_distances(
        graph.get_nodes(), source)

    while len(sorted_nodes) > 0:
        current_node = sorted_nodes.pop(0)

        if current_node[1] not in visited:
            visit(current_node[1], visited, graph,
                  dist, previous, sorted_nodes)

    return previous, dist
