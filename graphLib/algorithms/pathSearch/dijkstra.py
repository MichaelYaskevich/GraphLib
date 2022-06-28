def find_shortest_paths(graph, source):
    """
    Находит кратчайшие пути от исходной вершины до всех остальных вершин.

    :param graph: граф с положительными или нулевыми весами
    :param source: первая вершина в пути
    :return: итератор пар (результат get_path, расстояние до вершины)
    """

    from graphLib.algorithms.pathSearch.path_search_help_functions \
        import get_paths_from_source_to_all
    from graphLib.algorithms.pathSearch.dijkstra_help_functions \
        import get_prev_and_dist

    source = str(source)
    prev, dist = get_prev_and_dist(graph, source)
    return get_paths_from_source_to_all(source, prev, dist)


def find_shortest_path(graph, source, destination):
    """
    Находит кратчайшие пути от source до destination.

    :param graph: граф с положительными или нулевыми весами
    :param source: первая вершина в пути
    :param destination: последняя вершина в пути
    :return: кортеж (результат get_path, расстояние до вершины)
    """

    from graphLib.algorithms.pathSearch.path_search_help_functions \
        import get_path
    from graphLib.algorithms.pathSearch.dijkstra_help_functions \
        import get_prev_and_dist

    source, destination = str(source), str(destination)
    prev, dist = get_prev_and_dist(graph, source)
    return get_path(source, destination, prev), dist[destination]
