def find_shortest_paths(graph, source):
    """
    Находит кратчайшие пути в направленном ациклическом графе (DAG)
        от исходной вершины до всех остальных вершин.

    Граф может иметь ребра с отрицательными весами.

    :raises CycleError: если граф содержит цикл
    :param graph: Digraph
    :param source: первая вершина в пути
    :return: итератор пар (результат get_path, расстояние до вершины)
    """

    from src.algorithms.path_search_help_functions \
        import get_paths_from_source_to_all
    from src.algorithms.algorithm_for_DAG_help_functions \
        import get_prev_and_dist

    source = str(source)
    prev, dist = get_prev_and_dist(graph, source)
    return get_paths_from_source_to_all(source, prev, dist)


def topological_sort(adjacency_lists):
    """
    Сортировка вершин в топологическом порядке

    :raises CycleError: если граф содержит цикл

    :param adjacency_lists: словарь с вершинами в качестве ключей
        и списками смежных вершин в качестве значений
    :return: вершины в топологическом порядке
    """

    from src.algorithms.algorithm_for_DAG_help_functions \
        import initialize_input_degrees, initialize_queue, visit
    from src.data_structures.exception import CycleError

    deg_in = initialize_input_degrees(adjacency_lists)
    visited = initialize_queue(deg_in, adjacency_lists.keys())
    result = []

    while visited.qsize() != 0:
        v = visited.get()
        result.append(v)
        for w in adjacency_lists[v]:
            visit(deg_in, w, visited)

    if len(result) == len(adjacency_lists.keys()):
        return result

    message = '-'.join(get_cycle(adjacency_lists))
    raise CycleError(f"There is a cycle {message}")


def get_cycle(adjacency_lists):
    """
    Находит цикл в графе
    :param adjacency_lists: представление графа
    :return: цикл как список узлов или None
    """
    from src.algorithms.bellman_ford_help_functions \
        import build_cycle
    import queue

    prev = {}
    if len(adjacency_lists) < 2:
        return None
    q = queue.Queue()
    visited = {}
    for node in adjacency_lists.keys():
        if q.qsize() == 0:
            q.put(node)
            visited[node] = True
        else:
            visited[node] = False
    while q.qsize() != 0:
        node = q.get()
        for child in adjacency_lists[node]:
            prev[child] = node
            if visited[child]:
                return build_cycle(node, child, prev)
            else:
                q.put(child)
                visited[child] = True
    return None


def find_shortest_path(graph, source, destination):
    """
    Находит кратчайшие пути в направленном ациклическом графе (DAG)
        от source до destination.
    Граф может иметь ребра с отрицательными весами.

    :raises CycleError: если граф содержит цикл

    :param graph: Digraph
    :param source: первая вершина в пути
    :param destination: последняя вершина в пути
    :return: кортеж (результат get_path, расстояние до вершины)
    """

    from src.algorithms.path_search_help_functions \
        import get_path
    from src.algorithms.algorithm_for_DAG_help_functions \
        import get_prev_and_dist

    source, destination = str(source), str(destination)
    prev, dist = get_prev_and_dist(graph, source)
    return get_path(source, destination, prev), dist[destination]
