import unittest


from src.profiler.profiler import profile_all_algorithms
from src.interface.read_functions import read_graph_file
from graph_library.algorithms import dijkstra
from src.algorithms import bellman_ford, algorithm_for_DAG, floyd
from main import log_func


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


def handle_report_cmd(args):
    """Выолняет команду создания отчета из командной строки"""

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


def handle_find_path_cmd(args):
    """Выолняет команду поиска пути из командной строки"""

    graph, source, destination = read_graph_file(
        args.path[0], args.format[0])
    if destination == '-':
        alg = algs_all_paths[args.algorithm[0]]
        for result in alg(graph, source):
            process_alg_result(result)
    else:
        alg = algs_single_path[args.algorithm[0]]
        process_alg_result(
            alg(graph, source, destination))


def handle_test_cmd():
    """Выолняет команду запуска тестов из командной строки"""

    unittest.main(argv=['first-arg-is-ignored'], exit=False)


def process_alg_result(result):
    """
    Записывает полученный результат с помощью log_func

    :param result: результат поиска пути, возвращаемый всеми алгоритмами
    """

    path_or_info, distance = result
    ok, res = path_or_info
    if not ok:
        source, destination = res
        log_func(f'Нет пути из {source} в {destination}')
    else:
        log_func('path: ', '-'.join(res),
                 f"weight: {distance}")
