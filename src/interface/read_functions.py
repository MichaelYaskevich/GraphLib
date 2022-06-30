from src.data_structures.exception import FileInWrongFormatError


def read_graph_file(path, file_format):
    """
    Читает файл произвольного формата описывающий граф.

    :raises FileInWrongFormatError если в файл не подходит по формату

    :param path: путь к файлу
    :param file_format: тип формата al (adjacency lists) или wm (weight matrix)
    :return: кортеж из 3-х элементов graph, source, target
    """
    from src.data_structures.exception import FileInWrongFormatError

    try:
        with open(path, 'r') as graph_file:
            if file_format == 'al':
                result = read_adjacency_lists(graph_file.readline)
                if graph_file.read() != '':
                    raise FileInWrongFormatError('Неверный формат файла.')
                return result
            return read_weight_matrix(graph_file.readlines())
    except ValueError:
        raise FileInWrongFormatError('Неверный формат файла.')


def read_adjacency_lists(get_line):
    """
    Читает файл формата al (adjacency lists) описывающий граф.

    Формат al:\n
    4\n
    a b 25 c 4\n
    b 0\n
    c a 0 b 7\n
    d 0\n
    1\n
    4\n

    :param get_line: генератор строк
    :return: кортеж из 3-х элементов graph, source, destination
    """
    from src.data_structures.di_graph import DiGraph
    from src.data_structures.edge import Edge

    graph = DiGraph()
    n = int(get_line())
    for i in range(n):
        input_vertexes = get_line().split()
        current_node = input_vertexes[0]
        next_vertexes = []
        if current_node not in graph.get_nodes():
            graph.add_node(current_node)
        for j in range(2, len(input_vertexes), 2):
            node, weight = input_vertexes[j - 1], int(input_vertexes[j])
            next_vertexes.append(node)
            if node not in graph.get_nodes():
                graph.add_node(node)
            graph.add_edge(Edge(current_node, node, weight))
    source = get_line().strip()
    destination = get_line().strip()

    if source not in graph.get_nodes():
        raise FileInWrongFormatError('Неправильный формат файла:'
                                     ' source отсутствует в графе')
    if destination not in graph.get_nodes() and destination != '-':
        raise FileInWrongFormatError('Неправильный формат файла:'
                                     ' destination отсутствует в графе')

    return graph, source, destination


def read_weight_matrix(lines):
    """
    Читает файл формата wm (weight matrix) описывающий граф.

    Формат al:
    4\n
    0 1 0 1\n
    1 0 2 5\n
    1 3 0 -4\n
    0 0 5 0\n
    1\n
    4

    :param lines: все строки
    :return: кортеж из 3-х элементов graph, source, target
    """
    from src.data_structures.di_graph import DiGraph
    from src.data_structures.edge import Edge

    graph = DiGraph()
    source = lines[-2].strip()
    destination = lines[-1].strip()
    matrix_lines = lines[1:-2]

    for i, line in enumerate(matrix_lines):
        graph.add_node(str(i))
    for i, line in enumerate(matrix_lines):
        for j, value in enumerate(line.split()):
            if value == '-':
                continue
            val = int(value)
            graph.add_edge(Edge(str(i), str(j), val))

    if source not in graph.get_nodes():
        raise FileInWrongFormatError('Неправильный формат файла:'
                                     ' source отсутствует в графе')
    if destination not in graph.get_nodes() and destination != '-':
        raise FileInWrongFormatError('Неправильный формат файла:'
                                     ' destination отсутствует в графе')

    return graph, source, destination
