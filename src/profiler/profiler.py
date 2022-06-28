from pathlib import Path
from time import time
from memory_profiler import memory_usage

from main import log_func
from src.algorithms import dijkstra, bellman_ford, algorithm_for_DAG, floyd
from src.generator.generator import generate_graphs
from src.profiler.visualization_data import VisualizationData
from src.profiler.approximation import approximate
from src.profiler.statistic import Statistic
from src.profiler.visualization import make_docx, save_document

dummy_runs_count = 5
average_runs_count = 21
algs_all_paths = {
    'dijkstra': dijkstra.find_shortest_paths,
    'bellman_ford': bellman_ford.find_shortest_paths,
    'algorithm_for_dag': algorithm_for_DAG.find_shortest_paths,
    'floyd': floyd.find_shortest_paths_from_source
}
colors = ['black', 'red', 'green', 'blue']


def profile_all_algorithms(path, min_size, max_size):
    """
    Создание нового отчета о сравнении
    алгоритмов по использованию времени и памяти,
    основанного на случайно сгенерированных данных.

    :param path: путь для сохранения файла docx с результатами
    :param min_size: Минимальное количество узлов в генерируемых графах.
    :param max_size: Максимальное количество узлов в генерируемых графах.
    """

    memory = VisualizationData([], [], [])
    time = VisualizationData([], [], [])
    labels = []
    info_list = []
    graphs = generate_graphs(min_size, max_size)

    for label, alg in algs_all_paths.items():
        graph_sizes, time_statistics, mem_statistics, info = \
            profile(alg, graphs, label)

        labels.append(label)
        info_list.append(info)

        mem_data, mem_points, mem_conf_intervals = \
            adapt_for_visualization(graph_sizes, mem_statistics)
        memory.data_dictionaries.append(mem_data)
        memory.points_dictionaries.append(mem_points)
        memory.confidence_intervals.append(mem_conf_intervals)

        time_data, time_points, time_conf_intervals = \
            adapt_for_visualization(graph_sizes, time_statistics)
        time.data_dictionaries.append(time_data)
        time.points_dictionaries.append(time_points)
        time.confidence_intervals.append(time_conf_intervals)

    doc = make_docx(info_list, labels, colors, memory, time)

    save_document(doc, Path(path))


def adapt_for_visualization(graph_sizes, statistics):
    """
    Преобразует результаты в удобный для подачи в функции визуализации вид.

    :param graph_sizes: количества вершин графов
    :param statistics: экземпляры класса Statistic
    :return: точки функции, точки результатов, доверительные интервалы
    """

    n = len(graph_sizes)
    points_dict = {graph_sizes[i]: statistics[i].avg for i in range(n)}
    conf_intervals = {graph_sizes[i]: statistics[i].confidence_interval
                      for i in range(n)}
    x, y = approximate(
        graph_sizes, [statistics[i].avg for i in range(n)])
    data_dict = {x[i]: y[i] for i in range(len(x))}

    return data_dict, points_dict, conf_intervals


def profile(func, args, alg_name):
    """
    Проводит профилирование алгоритма на предоставленных графах.
    return result


def generate_worst_case_bf_graphs(min_size, max_size):
    result = []
    step = max(4, (max_size-min_size)//8)
    for i in range(max(min_size, 2), max_size, step):
        graph = generate_worst_case_graph_for_bellman_ford(i, 0, 1000)
        result.append((graph, randint(0, i - 1)))

    return result


def generate_best_case_bf_graphs(min_size, max_size):
    result = []
    step = max(4, (max_size-min_size)//8)
    for i in range(max(min_size, 2), max_size, step):
        graph = generate_best_case_graph_for_bellman_ford(i, 0, 1000)
        result.append((graph, i - 1))


    :param func: запускаемый алгоритм
    :param args: аргументы для алгоритма граф с вершиной - источником
    :param alg_name: название алгоритма
    :return: размеры графов, Statistic для времени и памяти, часть отчета
    """

    time_statistics = []
    memory_statistics = []
    graph_sizes = []
    for graph, source in args:
        time_stat, memory_stat = get_profiling_results(func, graph, source)
        time_statistics.append(time_stat)
        memory_statistics.append(memory_stat)
        graph_sizes.append(len(graph.get_nodes()))
    report_part = make_report(alg_name, time_statistics, memory_statistics)
    return graph_sizes, time_statistics, memory_statistics, report_part


def get_profiling_results(func, graph, source):
    """
    Проводит профилирование алгоритма на одном графе с холостыми запусками.

    :param func: запускаемый алгоритм
    :param graph: граф на котором запускается поиск
    :param source: вершина - источник для поиска
    :return: Statistic для времени, Statistic для памяти
    """

    for i in range(dummy_runs_count):
        func(graph, source)
    times, memory_us = get_times_and_memory_usage(func, graph, source)

    return Statistic(times), Statistic(memory_us)


def get_times_and_memory_usage(func, graph, source):
    """
    Проводит профилирование алгоритма на одном графе без холостых запусков.

    :param func: запускаемый алгоритм
    :param graph: граф на котором запускается поиск
    :param source: вершина - источник для поиска
    :return: замеры времени, замеры памяти
    """

    times = []
    for i in range(average_runs_count):
        current_run_start = time()
        count = 0
        while time() - current_run_start == 0.0:
            list(func(graph, source))
            count += 1
        times.append((time() - current_run_start) / count)

    memory_us = memory_usage(proc=lambda: list(func(graph, source)),
                             max_usage=False, backend="psutil",
                             include_children=True)
    return times, memory_us


def make_report(alg_name, time_statistics, memory_statistics):
    """
    Создает часть отчета для одного алгоритма.

    :param alg_name: название алгоритма
    :param time_statistics: экземпляры класса Statistic для времени
    :param memory_statistics: экземпляры класса Statistic для памяти
    :return: часть отчета
    """

    time_statistic = combine_data(time_statistics)
    memory_statistic = combine_data(memory_statistics)
    report_part = f"""
    -----------------> RESULTS OF PROFILING {alg_name} <-----------------\n\n
    ------------------------- TIME INFO -------------------------
    Average time spent is {time_statistic.avg} seconds
    Minimum time spent is {time_statistic.minimum} seconds
    Maximum time spent is {time_statistic.maximum} seconds
    Standard deviation is {time_statistic.std_deviation} seconds
    Confidence interval (delta) for time """ \
           f"""is {time_statistic.confidence_interval}'\n\n
    ------------------------ MEMORY INFO ------------------------
    Average memory usage is {memory_statistic.avg} MiB
    Minimum memory usage is {memory_statistic.minimum} MiB
    Maximum memory usage is {memory_statistic.maximum} MiB
    Standard deviation is {memory_statistic.std_deviation} MiB
    Confidence interval (delta) """ \
           f"""for memory is {memory_statistic.confidence_interval}\n\n\n\n
    """

    log_func(report_part)

    return report_part


def combine_data(statistics):
    """
    Объеденяет несколько экземпляров класса Statistic в один.

    :param statistics: экземпляры класса Statistic
    :return: экземпляр класса Statistic
    """

    arr = []
    for stat in statistics:
        arr += stat.array
    return Statistic(arr)
