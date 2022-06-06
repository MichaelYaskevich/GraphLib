import math
from random import randint
from time import time

from GraphLib.algorithms.pathSearch import dijkstra, bellman_ford, algorithm_for_DAG, floyd
from GraphLib.algorithms.pathSearch.algorithm_for_DAG import get_cycle
from GraphLib.generator.generator import generate_random_graph
from GraphLib.profiler.visualisation import approximate, visualize

dummy_runs_count = 5
average_runs_count = 21
t_param_values = {
    6: 2.5702,
    11: 2.2281,
    16: 2.1314,
    21: 2.0860,
    26: 2.0555,
    31: 2.0423,
    36: 2.0301,
    41: 2.0211,
    51: 2.0086,
    101: 1.9840
}


def profile_all_algorithms(path):
    algs_all_paths = {
        'dijkstra': dijkstra.find_shortest_paths,
                      'bellman_ford': bellman_ford.find_shortest_paths,
                      # 'algorithm_for_dag':
                      #     algorithm_for_DAG.find_shortest_paths,
                      'floyd': floyd.find_shortest_paths_from_source
    }
    data_dictionaries = []
    labels = []
    colors = ['black', 'yellow', 'green', 'blue']
    points_dictionaries = []
    confidence_intervals = []
    for label, alg in algs_all_paths.items():
        labels.append(label)
        avg_times, graph_sizes, conf_ints = profile(alg)
        confidence_intervals.append(
            {graph_sizes[i]: conf_ints[i]
             for i in range(len(graph_sizes))})
        points_dictionaries.append(
            {graph_sizes[i]: avg_times[i]
             for i in range(len(graph_sizes))})
        x, y = approximate(graph_sizes, avg_times)
        data_dictionaries.append({x[i]: y[i] for i in range(len(x))})

    visualize(data_dictionaries, labels, points_dictionaries, confidence_intervals, colors, path)


def profile(func):
    args = []
    i = 2
    while i <= 22:
        graph = generate_random_graph(i, i * 2, 0, 1000)
        args.append((graph, randint(0, i - 1)))
        i += 1
    avg_times = []
    graph_sizes = []
    conf_ints = []
    for graph, source in args:
        times, avg, minimum, std_dev, conf_int = get_profiling_results(func, graph, source)
        conf_ints.append(conf_int)
        avg_times.append(avg)
        graph_sizes.append(len(graph.get_nodes()))
        print_profiling_results(func, avg, minimum, std_dev, conf_int)
    return avg_times, graph_sizes, conf_ints


def get_profiling_results(func, graph, source):
    for i in range(dummy_runs_count):
        func(graph, source)
    times = get_times(func, graph, source)
    avg_time = calculate_average_time(times)
    min_time = calculate_min_time(times)
    std_deviation = calculate_standard_deviation(times, avg_time)
    confidence_interval = calculate_confidence_interval(times, std_deviation)
    return times, avg_time, min_time, std_deviation, confidence_interval


def get_times(func, graph, source):
    times = []
    for i in range(average_runs_count):
        current_run_start = time()
        list(func(graph, source))
        times.append(time() - current_run_start)
    return times


def calculate_min_time(times):
    return min(times)


def calculate_average_time(times):
    return sum(times) / len(times)


def calculate_standard_deviation(times, avg_time):
    s = 0
    for val in times:
        s += (val - avg_time) * (val - avg_time)

    return math.sqrt(s / (len(times) - 1))


def calculate_confidence_interval(times, std_deviation):
    return t_param_values[len(times)] * std_deviation / math.sqrt(len(times))


def result_to_str(time_in_seconds):
    return f'{int(time_in_seconds / 60)} minutes {time_in_seconds % 60} seconds'


def print_profiling_results(func, avg_time, min_time, std_deviation, confidence_interval):
    print(f'Results of profiling {func}:')
    print(f'Average time spent is {avg_time} seconds, which equals to {result_to_str(avg_time)}')
    print(f'Minimum time spent is {min_time} seconds, which equals to {result_to_str(min_time)}')
    print(f'Standard deviation is {std_deviation} seconds, which equals to {result_to_str(std_deviation)}')
    print(f'Confidence interval (delta) is {confidence_interval}, which equals to {result_to_str(confidence_interval)}')
