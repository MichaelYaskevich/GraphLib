import argparse

from src.interface import file_formats


def make_parser():
    """
    Создает парсер со всеми нужными подпарсерами

    :return: argparse.ArgumentParser
    """

    description = """
    find_path: Поиск пути в графе от одной вершины до всех
        или путь от одной вершины до конкретной вершины.
    test: Запуск всех тестов проекта.
    report: Создание нового отчета о сравнении алгоритмов по
    использованию времени и памяти,
        основанного на случайно сгенерированных данных.
    visualize: Визуализация пути в графе с помощью библиотеки networkx

    Чтобы вызвать help определенного подпарсера, нужно написать python
    main.py имя_подпарсера -h
    """

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=description)

    subparsers = parser.add_subparsers(help='', dest='name')

    add_find_path_parser(subparsers)
    add_test_parser(subparsers)
    add_report_parser(subparsers)
    add_visualize_parser(subparsers)

    return parser


def add_visualize_parser(subparsers):
    """Добавляет подпарсер graph_visualization"""

    al_format = file_formats.graph_adjacency_list_file_format
    wm_format = file_formats.graph_weight_matrix_file_format
    visualize_parser = subparsers.add_parser(
        'visualize',
        description=f'Визуализация пути в графе от одной вершины '
                    f'до другой вершины\n'
                    f'Для запуска необходимо указать путь '
                    f'к txt файлу, который описывает граф\n'
                    f'В файле обязательно должна быть указана начальная '
                    f'и конечная вершина\n'
                    f'Граф может быть описан в следующих форматах:\n\n'
                    f'====Списки смежности====\n{al_format}'
                    f'\n\n====Матрица весов====\n{wm_format}',
        formatter_class=argparse.RawDescriptionHelpFormatter)
    visualize_parser.add_argument(
        'path', type=str, nargs=1,
        help=f'Абсолютный или относительный путь до файла, описывающего граф')
    visualize_parser.add_argument(
        'format', type=str, nargs=1, choices=['al', 'wm'],
        help='Выберите формат, в котором описан граф: \n'
             '"al" означает adjacency list, а\n'
             ' "wm" означает weight matrix')
    visualize_parser.add_argument(
        'algorithm', type=str, nargs=1,
        choices=['dijkstra', 'bellman_ford',
                 'algorithm_for_dag', 'floyd'],
        help=f'Алгоритм, который вы хотите использовать')


def add_test_parser(subparsers):
    """Добавляет подпарсер test"""

    subparsers.add_parser(
        'test', description='Запуск всех тестов проекта.',
        formatter_class=argparse.RawDescriptionHelpFormatter)


def add_report_parser(subparsers):
    """Добавляет подпарсер report"""

    report_parser = subparsers.add_parser(
        'report',
        description="""Создание нового отчета о сравнении
        алгоритмов по использованию времени и памяти,
        основанного на случайно сгенерированных данных.""",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    report_parser.add_argument(
        'path', type=str, nargs=1,
        help='Абсолютный или относительный путь, '
             'по которому следует сохранить отчет.')
    report_parser.add_argument(
        'min_graph_size', type=int, nargs=1,
        help='Минимальное количество узлов в генерируемых графах.')
    report_parser.add_argument(
        'max_graph_size', type=int, nargs=1,
        help='Максимальное количество узлов в генерируемых графах.')


def add_find_path_parser(subparsers):
    """Добавляет подпарсер find_path"""

    al_format = file_formats.graph_adjacency_list_file_format
    wm_format = file_formats.graph_weight_matrix_file_format
    find_path_parser = subparsers.add_parser(
        'find_path',
        description=f'Поиск пути в графе от одной вершины до всех '
                    f'или путь от одной вершины до конкретной вершины.\n'
                    f'Для запуска необходимо указать путь '
                    f'к txt файлу, который описывает граф.\n'
                    f'Граф может быть описан в следующих форматах:\n'
                    f'====Списки смежности====\n{al_format}'
                    f'\n\n====Матрица весов====\n{wm_format}',
        formatter_class=argparse.RawDescriptionHelpFormatter)
    find_path_parser.add_argument(
        'path', type=str, nargs=1,
        help=f'Абсолютный или относительный путь до файла с графом.')
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
