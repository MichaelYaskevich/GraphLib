import math

from src.data_structures.di_graph import DiGraph
from src.data_structures.exception import NegativeCycleError


def find_negative_cycle(graph, dist, previous):
    """
    Находит цикл отрицательного веса.

    :raises NegativeCycleError: когда отрицательный цикл найден

    :param graph: граф
    :param dist: массив расстояний
    :param previous: массив предыдущих
    """

    for w, v in get_better_edges(graph, dist):
        raise_error(w, v, previous)


def update_distances(graph: DiGraph, dist, previous):
    """
    Обновляет все возможные дистанции.

    :param graph: граф
    :param dist: массив расстояний
    :param previous: массив предыдущих
    """

    for w, v in get_better_edges(graph, dist):
        edge = graph.get_incident_edge(w, v)
        update_dist(w, v, dist, edge.weight, previous)


def update_dist(current, neighbor, dist, weight, previous):
    """
    Обновляет массив растояний и массив предыдущих

    :param current: текущая вершина
    :param neighbor: соседняя вершина
    :param weight: вес ребра между current и neighbor
    :param dist: массив расстояний
    :param previous: массив предыдущих
    """

    dist[neighbor] = dist[current] + weight
    previous[neighbor] = current


def get_better_edges(graph: DiGraph, dist):
    """
    Находит ребра через которые можно пройти,
    чтобы уменьшить расстояние

    :param graph: граф
    :param dist: массив расстояний
    :return: итератор ребер
    """

    for w, v in graph.get_edges():
        edge = graph.get_incident_edge(w, v)
        if dist[w] + edge.weight < dist[v]:
            yield w, v


def raise_error(prev, source, previous):
    """
    Выбрасывает ислючение.

    :raises NegativeCycleError: всегда
    """

    message = '-'.join(build_cycle(prev, source, previous))
    raise NegativeCycleError(f"Найден цикл отрицательного веса {message}")


def build_cycle(prev, source, previous):
    """
    Строит цикл.

    :raises Exception: если не хватает информации для построения цикла

    :param prev: массив предыдущих
    :param source: вершина-источник
    :param previous: вершина-конец
    :return: цикл
    """

    path = [source, prev]
    current = prev
    while current != source:
        if current not in previous:
            raise Exception("не хватает информации для построения цикла")
        current = previous[current]
        path.append(current)

    path.reverse()
    return path


def initialise_distances(nodes, source):
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


def get_prev_and_dist(graph: DiGraph, source):
    """
    Находит кратчайшие пути от source до всех вершин.

    :raises NegativeCycleError: когда найден цикл отрицательной длины

    :param graph: граф
    :param source: вершина-источник
    :return: массив предудущих, массив расстоний
    """

    previous = {source: None}
    dist = initialise_distances(
        graph.get_nodes(), source)

    for _ in range(1, len(graph.get_nodes())):
        update_distances(graph, dist, previous)

    find_negative_cycle(graph, dist, previous)

    return previous, dist
