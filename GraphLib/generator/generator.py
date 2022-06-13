from random import shuffle, uniform
from GraphLib.dataStructures.di_graph import DiGraph, is_cyclic
from GraphLib.dataStructures.edge import Edge
from random import randint


def generate_random_graph(nodes_count, min_weight, max_weight):
    """
    Создает случайный граф.

    :param nodes_count: количество вершин в графе
    :param min_weight: минимальный вес ребра в графе
    :param max_weight: максимальный вес ребра в графе
    :return: граф
    """

    if nodes_count <= 0:
        raise ValueError(f"Inappropriate value for nodes_count: "
                         f"{nodes_count}, nodes_count "
                         f"can't be zero or less")
    if min_weight > max_weight:
        raise ValueError(f'Min_weight parameter ({min_weight}) '
                         f'is bigger than max_weight ({max_weight})')

    graph = DiGraph()
    nodes = [str(x) for x in range(nodes_count)]

    for node in nodes:
        graph.add_node(node)

    for x in nodes:
        for y in nodes:
            if x != y:
                edge = Edge(x, y, uniform(min_weight, max_weight))
                graph.add_edge(edge)
                if is_cyclic(graph):
                    graph.delete_edge(edge)

    return graph


def generate_worst_case_graph_for_bellman_ford(
        nodes_count, min_weight, max_weight):
    graph = DiGraph()
    nodes = [str(x) for x in range(nodes_count)]

    for node in nodes:
        graph.add_node(node)

    for x in nodes:
        for y in nodes:
            if x != y:
                edge = Edge(x, y, uniform(min_weight, max_weight))
                graph.add_edge(edge)

    return graph


def generate_best_case_graph_for_bellman_ford(
        nodes_count, min_weight, max_weight):
    graph = DiGraph()
    nodes = [str(x) for x in range(nodes_count)]

    for node in nodes:
        graph.add_node(node)

    for x in range(nodes_count - 1):
        graph.add_edge(
            Edge(str(x), str(x + 1),
                 uniform(min_weight, max_weight)))

    return graph


def generate_graphs(min_size, max_size):
    """
    Создает случайные графы с вершинами-источниками для поиска

    :param min_size: Минимальный размер графа
    :param max_size: Максимальный размер графа
    :return: граф, вершина-источник
    """

    result = []
    step = max(4, (max_size - min_size) // 8)
    for i in range(max(min_size, 2), max_size, step):
        graph = generate_random_graph(i, 0, 1000)
        result.append((graph, randint(0, i - 1)))
    return result
