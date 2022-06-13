from GraphLib.dataStructures.di_graph import DiGraph


def find_shortest_paths(graph: DiGraph, source):
    """
    Находит кратчайшие пути от исходной вершины до всех остальных вершин.
    Граф может иметь ребра с отрицательными весами.

    :выдает NegativeCycleError: если в графе есть отрицательные циклы

    :param graph: DiGraph
    :param source: первая вершина в пути
    :return: итератор пар (результат get_path, расстояние до вершины)
    """

    from GraphLib.algorithms.pathSearch.path_search_help_functions \
        import get_paths_from_source_to_all
    from GraphLib.algorithms.pathSearch.bellman_ford_help_functions \
        import get_prev_and_dist

    source = str(source)
    prev, dist = get_prev_and_dist(graph, source)
    return get_paths_from_source_to_all(source, prev, dist)


def find_shortest_path(graph: DiGraph, source, destination):
    """
    Находит кратчайшие пути от исходной вершины до всех остальных вершин.
    Граф может иметь ребра с отрицательными весами.

    :выдает NegativeCycleError: если в графе есть отрицательные циклы

    :param graph: DiGraph
    :param source: первая вершина в пути
    :param destination: последняя вершина в пути
    :return: кортеж (результат get_path, расстояние до вершины)
    """

    from GraphLib.algorithms.pathSearch.path_search_help_functions \
        import get_path
    from GraphLib.algorithms.pathSearch.bellman_ford_help_functions \
        import get_prev_and_dist

    source, destination = str(source), str(destination)
    prev, dist = get_prev_and_dist(graph, source)
    return get_path(source, destination, prev), dist[destination]
