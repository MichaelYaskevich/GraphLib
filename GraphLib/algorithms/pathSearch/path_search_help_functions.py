def get_paths_from_source_to_all(source, previous, distances):
    for node in distances.keys():
        if node != source:
            yield get_path(source, node, previous), distances[node]


def get_path(source, destination, previous: dict) -> list:
    current = previous[destination]
    path = [destination, current]
    while current != source:
        current = previous[current]
        path.append(current)
    path.reverse()

    return path
