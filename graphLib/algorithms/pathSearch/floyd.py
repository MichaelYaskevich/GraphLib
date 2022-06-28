def find_shortest_paths_from_all_to_all(graph):
    """
    Этот алгоритм находит кратчайшие пути в направленном взвешенном графе
        с положительными или отрицательными весами ребер.

    :param graph: DiGraph
    :return: матрица расстояний и матрица предыдущих
    """

    from graphLib.algorithms.pathSearch.floyd_help_functions import \
        initialise_matrix_of_distances, \
        update_distance, \
        initialise_prior_matrix

    distances = initialise_matrix_of_distances(graph)

    prior_matrix = initialise_prior_matrix(graph)
    for w in graph.get_nodes():
        for i in graph.get_nodes():
            for j in graph.get_nodes():
                update_distance(distances, prior_matrix, w, i, j)

    return distances, prior_matrix


def find_shortest_paths_from_source(graph, source):
    """
    Этот алгоритм находит кратчайшие пути от исходного узла
    ко всем другим узлам в направленном взвешенном графе
    с положительными или отрицательными весами ребер.

    :param graph: DiGraph
    :param source: первый узел в пути
    :return: итератор пар (результат get_path, расстояние до вершины)
    """

    source = str(source)
    distances, prior_matrix = find_shortest_paths_from_all_to_all(graph)
    for node in graph.get_nodes():
        if node != source:
            yield get_path(
                source, node, prior_matrix), distances[source][node]


def find_shortest_path(graph, source, destination):
    """
    Этот алгоритм находит кратчайший путь
    от узла-источника до узла назначения.

    :param graph: DiGraph
    :param source: первый узел в пути
    :param destination: последний узел в пути
    :return: кортеж (результат get_path, расстояние до вершины)
    """

    source, destination = str(source), str(destination)
    dist, prior_matrix = find_shortest_paths_from_all_to_all(graph)
    return get_path(source, destination, prior_matrix), dist[destination]


def get_path(source, destination, prior_matrix):
    """
    Этот алгоритм находит кратчайший путь
    от source до destination.

    :param source: первый узел в пути
    :param destination: последний узел в пути
    :param prior_matrix: матрица, в которой хранится информация о пути
    :return: путь от источника к пункту назначения или None
    """

    intermediate_node = prior_matrix[source][destination]
    if intermediate_node == destination:
        if destination == source:
            return [source]
        return [source, destination]
    if intermediate_node is None:
        return None
    path: list = get_path(source, intermediate_node, prior_matrix)[:-1]
    for v in get_path(intermediate_node, destination, prior_matrix):
        path.append(v)
    return path
