import math
from time import time

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


def profile(func, args_for_different_setups):
    for args in args_for_different_setups:
        times, avg, minimum, std_dev, conf_int = get_profiling_results(func, args)
        print_profiling_results(func, avg, minimum, std_dev, conf_int)
        ### здесь будет выводить графики


def get_profiling_results(func, args):
    for i in range(dummy_runs_count):
        func(args)
    start_time = time()
    times = []
    for i in range(average_runs_count):
        current_run_start = time()
        func(args)
        times.append(time() - current_run_start)
    end_time = time()
    avg_time = (end_time - start_time) / average_runs_count
    min_time = min(times)
    std_deviation = calculate_standard_deviation(times, avg_time)
    confidence_interval = calculate_confidence_interval(times, std_deviation)
    return times, avg_time, min_time, std_deviation, confidence_interval


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
