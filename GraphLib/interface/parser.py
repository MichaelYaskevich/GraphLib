import argparse
import unittest

from GraphLib.algorithms.pathSearch \
    import dijkstra, bellman_ford, algorithm_for_DAG, floyd
from GraphLib.interface.read_adjacency_lists import read_adjacency_lists
from GraphLib.interface.read_weight_matrix import read_weight_matrix
from GraphLib.profiler.profiler import profile_all_algorithms

graph_adjacency_list_file_format = '''
В первой строке указано количество вершин N
В каждой из следующих N строк указна запись для каждой вершины в формате:
i j weight(i, j) k weight(i, k) ... m weight(i, m)
где j, k, ..., m соседи узла i
В предпоследней строке узел являющийся началом пути
В последней строке узел являющийся концом пути или '-' если вы хотите увидеть пути от источника до всех вершин

Пример:
4
a b 25 c 4
b 0
c a 0 b 7
d 0
a
-'''

graph_weight_matrix_file_format = '''
В первой строке указано количество вершин N
В следующих N строках представлен граф как матрица весов,
    где '-' означает, что ребра не существует
В предпоследней строке узел являющийся началом пути
В последней строке узел являющийся концом пути

Пример:
4
0 1 0 1
1 0 2 5
1 3 0 -4
0 0 5 0
1
4
'''

algs_all_paths = {'dijkstra': dijkstra.find_shortest_paths,
                  'bellman_ford': bellman_ford.find_shortest_paths,
                  'algorithm_for_dag':
                      algorithm_for_DAG.find_shortest_paths,
                  'floyd': floyd.find_shortest_paths_from_source}
algs_single_path = {'dijkstra': dijkstra.find_shortest_path,
                    'bellman_ford': bellman_ford.find_shortest_path,
                    'algorithm_for_dag':
                        algorithm_for_DAG.find_shortest_path,
                    'floyd': floyd.find_shortest_path}

log_func = print


def run():
    try:
        parser = make_parser()
        args = parser.parse_args()

        if args.name == 'report':
            process_report_cmd(args)
        elif args.name == 'test':
            unittest.main(argv=['first-arg-is-ignored'], exit=False)
        else:
            process_find_path_cmd(args)
    except Exception as e:
        log_func(e.args[0])


def process_report_cmd(args):
    min_size, max_size = args.min_graph_size[0], args.max_graph_size[0]
    if max_size - min_size < 10:
        log_func(f'Укажите диапазон больше чем '
                 f'{min_size}-{max_size} '
                 f'чтобы сделать более точные вычисления')
    elif max_size > 60:
        log_func(f'{max_size} не должен быть больше чем 60, '
                 f'чтобы профилирование не заняло много времени')
    else:
        profile_all_algorithms(args.path[0], min_size, max_size)


def process_find_path_cmd(args):
    graph, source, destination = read_graph_file(args)
    if destination == '-':
        alg = algs_all_paths[args.algorithm[0]]
        for result in alg(graph, source):
            process_alg_result(result)
    else:
        alg = algs_single_path[args.algorithm[0]]
        process_alg_result(
            alg(graph, source, destination))


def read_graph_file(args):
    with open(args.path[0], 'r') as graph_file:
        if args.format[0] == 'al':
            graph = read_adjacency_lists(graph_file.readline)
            if graph_file.read() != '':
                raise FileInWrongFormatError('Неверный формат файла.')
            return graph
        return read_weight_matrix(graph_file.readlines())


def process_alg_result(result):
    path_or_info, distance = result
    ok, result = path_or_info
    if not ok:
        source, destination = result
        log_func(f'Нет пути из {source} в {destination}')
    else:
        log_func('path: ', '-'.join(result),
                 f"weight: {distance}")


def make_parser():
    description = """
    find_path: Поиск пути в графе от одной вершины до всех 
        или путь от одной вершины до конкретной вершины.
    test: Запуск всех тестов проекта.
    report: Создание нового отчета о сравнении алгоритмов по использованию времени и памяти, 
        основанного на случайно сгенерированных данных.
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=description)

    subparsers = parser.add_subparsers(help='', dest='name')

    add_find_path_parser(subparsers)
    add_test_parser(subparsers)
    add_report_parser(subparsers)

    return parser


def add_test_parser(subparsers):
    subparsers.add_parser(
        'test', description='Запуск всех тестов проекта.',
        formatter_class=argparse.RawDescriptionHelpFormatter)


def add_report_parser(subparsers):
    report_parser = subparsers.add_parser(
        'report',
        description="""Создание нового отчета о сравнении алгоритмов по использованию времени и памяти, 
        основанного на случайно сгенерированных данных.""",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    report_parser.add_argument(
        'path', type=str, nargs=1,
        help='Путь по которому следует сохранить отчет.')
    report_parser.add_argument(
        'min_graph_size', type=int, nargs=1,
        help='Минимальное количество узлов в генерируемых графах.')
    report_parser.add_argument(
        'max_graph_size', type=int, nargs=1,
        help='Максимальное количество узлов в генерируемых графах.')


def add_find_path_parser(subparsers):
    find_path_parser = subparsers.add_parser(
        'find_path',
        description=f'Поиск пути в графе от одной вершины до всех '
                    f'или путь от одной вершины до конкретной вершины.\n'
                    f'Для запуска необходимо указать путь к txt файлу, который описывает граф.\n'
                    f'Граф может быть описан в следующих форматах:\n'
                    f'====Списки смежности====\n{graph_adjacency_list_file_format}'
                    f'\n\n====Матрица весов====\n{graph_weight_matrix_file_format}',
        formatter_class=argparse.RawDescriptionHelpFormatter)
    find_path_parser.add_argument(
        'path', type=str, nargs=1,
        help=f'Полный путь до файла с графом.')
    find_path_parser.add_argument(
        'format', type=str, nargs=1, choices=['al', 'wm'],
        help='Выберете формат в котором описан граф: \n'
             '"al" означает adjacency list, а\n'
             ' "wm" означает weight matrix.')
    find_path_parser.add_argument(
        'algorithm', type=str, nargs=1,
        choices=['dijkstra', 'bellman_ford',
                 'algorithm_for_dag', 'floyd'],
        help=f'Алгоритм, который вы хотите использовать.')
