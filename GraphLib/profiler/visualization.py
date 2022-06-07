from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns


def visualize_memory(data_dictionaries: list, labels: list,
                     points_dictionaries, confidence_intervals,
                     colors, pdf_or_path):
    plt.figure(figsize=(16, 6))
    plt.title("Memory performance research")
    plt.xlabel("data size, nodes count")
    plt.ylabel("memory, MiB")
    visualize(data_dictionaries, labels,
              points_dictionaries, confidence_intervals, colors, pdf_or_path)


def visualize_time(data_dictionaries: list, labels: list,
                   points_dictionaries, confidence_intervals,
                   colors, pdf_or_path):
    plt.figure(figsize=(16, 6))
    plt.title("Time performance research")
    plt.xlabel("data size, nodes count")
    plt.ylabel("time, seconds")
    visualize(data_dictionaries, labels,
              points_dictionaries, confidence_intervals,
              colors, pdf_or_path)


def visualize(data_dictionaries: list, labels: list,
              points_dictionaries, confidence_intervals,
              colors, pdf_or_path):
    for i in range(len(data_dictionaries)):
        sns.lineplot(data=data_dictionaries[i],
                     label=labels[i], color=colors[i])
        sns.scatterplot(data=points_dictionaries[i],
                        s=100, color=colors[i])
        for key, value in points_dictionaries[i].items():
            shift = confidence_intervals[i][key] / 2.0
            plt.plot([key, key], [value - shift, value + shift],
                     color=colors[i])
    if isinstance(pdf_or_path, Path):
        plt.savefig(pdf_or_path)
    else:
        pdf_or_path.savefig()
