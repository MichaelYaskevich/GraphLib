import math

from graphLib.dataStructures.di_graph import DiGraph


def initialise_matrix_of_distances(graph: DiGraph):
    """
    Создает матрицу расстояний.

    :param graph: граф, по которому строить матрицу
    :return: матрица расстояний
    """

    distances = {}
    for i in graph.get_nodes():
        distances[i] = ({})
        for j in graph.get_nodes():
            distances[i][j] = math.inf

    for e in graph.get_edges():
        a, b = e
        distances[a][b] = e.weight

    for v in graph.get_nodes():
        distances[v][v] = 0

    return distances


def update_distance(distances, prior_matrix, w, i, j):
    """
    Обновляет расстояние в матрице расстояний при соблюдении условия.

    :param distances: матрица расстояний
    :param prior_matrix: матрица предыдущих
    :param w: индекс вершины проверяемой на уменьшение длины пути
    :param i: индекс начала пути
    :param j: индекс конца пути
    """

    if distances[i][w] + distances[w][j] < distances[i][j]:
        distances[i][j] = distances[i][w] + distances[w][j]
        prior_matrix[i][j] = prior_matrix[i][w]


def initialise_prior_matrix(graph: DiGraph):
    """
    Создает матрицу предыдущих.

    :param graph: граф, по которому строить матрицу
    :return: матрица предудущих
    """

    matrix = {}
    for i in graph.get_nodes():
        matrix[i] = {}
        for j in graph.get_nodes():
            if i == j or j in graph.adjacency_lists[i]:
                matrix[i][j] = j
            else:
                matrix[i][j] = None
    return matrix
