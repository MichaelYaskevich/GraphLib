import math
import queue

from src.algorithms.algorithm_for_DAG import topological_sort
from src.data_structures.di_graph import DiGraph


def initialize_input_degrees(adjacency_lists):
    """
    Создает словарь ключ-вершина, значение-степень захода

    :param adjacency_lists: списки смежности графа
    :return: словарь
    """

    deg_in_dict = {v: 0 for v in adjacency_lists.keys()}

    for vertex in adjacency_lists.keys():
        for neighbor in adjacency_lists[vertex]:
            deg_in_dict[neighbor] += 1

    return deg_in_dict


def initialize_queue(deg_in_list, nodes):
    """
    Создает очередь из вершин с нулевой степенью захода

    :param deg_in_list: словарь возвращаемый initialize_input_degrees
    :param nodes: вершины графа
    :return очередь:
    """

    q = queue.Queue()

    for vertex in nodes:
        if deg_in_list[vertex] == 0:
            q.put(vertex)

    return q


def visit(deg_in_list, vertex, visited_queue):
    """
    Посещает вершины с нулевой степень захода.

    :param deg_in_list: словарь возвращаемый initialize_input_degrees
    :param vertex: вершина проверяемая на степень захода
    :param visited_queue: очередь из вершин с нулевой степенью захода
    """

    deg_in_list[vertex] -= 1
    if deg_in_list[vertex] == 0:
        visited_queue.put(vertex)


def update_distances(
        graph: DiGraph, distances: dict, previous: dict, vertex):
    """
    Обновляет расстояния до соседей vertex.

    :param graph: граф
    :param distances: массив расстояний
    :param previous: массив предыдущих
    :param vertex: вершина расстояния до соседей которой обновляем
    """

    for w in graph.adjacency_lists[vertex]:
        edge = graph.get_incident_edge(vertex, w)
        if distances[vertex] + edge.weight < distances[w]:
            distances[w] = distances[vertex] + edge.weight
            previous[w] = vertex


def find_vertex_index(vertexes, vertex):
    """
    Находит индекс вершины vertex в массиве vertexes.

    :param vertexes: массив вершин
    :param vertex: вершина, индекс которой ищем
    :return: индекс vertex
    """

    index = -1
    for i, v in enumerate(vertexes):
        if v == vertex:
            index = i
            break

    return index


def find_shortest_paths(sorted_vertexes: list, graph: DiGraph, source):
    """
    Находит кратчайший путь от исходной вершины до всех остальных.

    :param sorted_vertexes: вершины в топологическом порядке
    :param graph: Digraph
    :param source: первая вершина в пути
    :return: дерево кратчайших путей с расстояниями
    """

    nodes_count = len(graph.get_nodes())
    dist = {v: math.inf for v in graph.get_nodes()}
    dist[source] = 0
    prev = {source: None}

    source_index = find_vertex_index(sorted_vertexes, source)

    for i in range(source_index, nodes_count):
        vertex = sorted_vertexes[i]
        update_distances(graph, dist, prev, vertex)

    return prev, dist


def get_prev_and_dist(graph: DiGraph, source):
    """
    Находит кратчайшие пути от source до всех вершин.

    :raises CycleError: если граф содержит цикл

    :param graph: граф
    :param source: вершина-источник
    :return: массив предудущих, массив расстоний
    """

    sorted_vertexes = topological_sort(graph.adjacency_lists)

    return find_shortest_paths(sorted_vertexes, graph, source)
