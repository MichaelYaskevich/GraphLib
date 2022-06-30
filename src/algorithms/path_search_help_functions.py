def get_paths_from_source_to_all(source, previous, distances):
    """
    Ищет пути в графе от источника до всех.

    :param source: вершина - источник
    :param previous: массив предыдущих
    :param distances: массив расстояний
    :return: итератор пар (результат get_path, расстояние до вершины)
    """

    for node in distances.keys():
        if node != source:
            yield get_path(source, node, previous), distances[node]


def get_path(source, destination, previous: dict):
    """
    Ищет путь от source до destination.

    :param source: вершина-начало
    :param destination: вершина-конец
    :param previous: массив предыдущих
    :return: кортеж (False, (source, destination)) или (True, path)
    """

    if destination not in previous:
        return False, (source, destination)
    current = previous[destination]
    path = [destination, current]
    while current != source:
        current = previous[current]
        path.append(current)
    path.reverse()

    return True, path
