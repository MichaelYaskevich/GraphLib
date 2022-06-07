import math
from random import randint
from time import time

from matplotlib.backends.backend_pdf import PdfPages
from memory_profiler import memory_usage

from GraphLib.algorithms.pathSearch import dijkstra, bellman_ford, algorithm_for_DAG, floyd
from GraphLib.generator.generator import generate_random_graph
from GraphLib.profiler.approximation import approximate
from GraphLib.profiler.statistic import Statistic
from GraphLib.profiler.visualization import visualize_time, visualize_memory

dummy_runs_count = 5
average_runs_count = 21


def profile_all_algorithms(path):
    algs_all_paths = {
        'dijkstra': dijkstra.find_shortest_paths,
        'bellman_ford': bellman_ford.find_shortest_paths,
        # 'algorithm_for_dag':
        #     algorithm_for_DAG.find_shortest_paths,
        'floyd': floyd.find_shortest_paths_from_source
    }
    time_data_dictionaries = []
    mem_data_dictionaries = []
    labels = []
    colors = ['black', 'red', 'green', 'blue']
    time_points_dicts = []
    time_conf_intervals = []
    mem_conf_intervals = []
    mem_points_dicts = []
    for label, alg in algs_all_paths.items():
        labels.append(label)
        graph_sizes, time_statistics, memory_statistics = profile(alg)

        mem_conf_intervals.append(
            {graph_sizes[i]: memory_statistics[i].confidence_interval
             for i in range(len(graph_sizes))})
        mem_points_dicts.append(
            {graph_sizes[i]: memory_statistics[i].avg
             for i in range(len(graph_sizes))})
        x, y = approximate(graph_sizes,
                           [memory_statistics[i].avg
                            for i in range(len(graph_sizes))])
        mem_data_dictionaries.append(
            {x[i]: y[i] for i in range(len(x))})

        time_conf_intervals.append(
            {graph_sizes[i]: time_statistics[i].confidence_interval
             for i in range(len(graph_sizes))})
        time_points_dicts.append(
            {graph_sizes[i]: time_statistics[i].avg
             for i in range(len(graph_sizes))})
        x, y = approximate(graph_sizes,
                           [time_statistics[i].avg
                            for i in range(len(graph_sizes))])
        time_data_dictionaries.append({x[i]: y[i] for i in range(len(x))})

    with PdfPages(path) as pdf:
        visualize_memory(mem_data_dictionaries, labels, mem_points_dicts, mem_conf_intervals, colors, pdf)
        visualize_time(time_data_dictionaries, labels, time_points_dicts, time_conf_intervals, colors, pdf)


def profile(func):
    args = []
    for i in range(10, 31, 4):
        graph = generate_random_graph(i, i * 2, 0, 1000)
        args.append((graph, randint(0, i - 1)))

    time_statistics = []
    memory_statistics = []
    graph_sizes = []
    for graph, source in args:
        time_statistic, memory_statistic = get_profiling_results(func, graph, source)
        time_statistics.append(time_statistic)
        memory_statistics.append(memory_statistic)
        graph_sizes.append(len(graph.get_nodes()))
        print_profiling_results(func, time_statistic, memory_statistic)
    return graph_sizes, time_statistics, memory_statistics


def get_profiling_results(func, graph, source):
    for i in range(dummy_runs_count):
        func(graph, source)
    times, memory_us = get_times_and_memory_usage(func, graph, source)
    memory_statistic = Statistic(memory_us)
    time_statistic = Statistic(times)
    return time_statistic, memory_statistic


def get_times_and_memory_usage(func, graph, source):
    times = []
    for i in range(average_runs_count):
        current_run_start = time()
        list(func(graph, source))
        times.append(time() - current_run_start)
    memory_us = memory_usage(proc=lambda: list(func(graph, source)),
                             max_usage=False, backend="psutil",
                             include_children=True)
    return times, memory_us


def result_to_str(time_in_seconds):
    return f'{int(time_in_seconds / 60)} minutes {time_in_seconds % 60} seconds'


def print_profiling_results(func, time_statistic, memory_statistic):
    print(f'Results of profiling {func}:')

    print(f'Average time spent is {time_statistic.avg} seconds, '
          f'which equals to {result_to_str(time_statistic.avg)}')
    print(f'Minimum time spent is {time_statistic.minimum} seconds, '
          f'which equals to {result_to_str(time_statistic.minimum)}')
    print(f'maximum time spent is {time_statistic.maximum} seconds, '
          f'which equals to {result_to_str(time_statistic.maximum)}')
    print(f'Standard deviation is {time_statistic.std_deviation} seconds, '
          f'which equals to {result_to_str(time_statistic.std_deviation)}')
    print(f'Confidence interval (delta) for time is {time_statistic.confidence_interval}, '
          f'which equals to {result_to_str(time_statistic.confidence_interval)}')

    print(f'Average memory usage is {memory_statistic.avg} MiB')
    print(f'Minimum memory usage is {memory_statistic.minimum} MiB')
    print(f'Maximum memory usage is {memory_statistic.maximum} MiB')
    print(f'Standard deviation is {memory_statistic.std_deviation} MiB')
    print(f'Confidence interval (delta) for memory is {memory_statistic.confidence_interval}')
