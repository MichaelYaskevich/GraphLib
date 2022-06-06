import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def approximate(graph_size_array, time_results_array):
    train_X = transform_data_for_linear_model(graph_size_array)
    train_y = time_results_array
    model = LinearRegression()

    model.fit(train_X, train_y)

    segmentation = []
    steps = len(graph_size_array) * 10
    for i in range(1, steps + 1):
        segmentation.append(i * 0.1)
    test_X = transform_data_for_linear_model(segmentation)

    test_y = model.predict(test_X)

    return segmentation, test_y


def transform_data_for_linear_model(data):
    transformed_data = []
    for i in range(len(data)):
        transformed_data.append([data[i]])
    return PolynomialFeatures(degree=3).fit_transform(transformed_data)


def visualize(data_dictionaries: list, labels: list, points_dictionaries, confidence_intervals, colors, path):
    plt.figure(figsize=(16, 6))
    plt.title("Time performance research")
    for i in range(len(data_dictionaries)):
        sns.lineplot(data=data_dictionaries[i], label=labels[i], color=colors[i])
        sns.scatterplot(data=points_dictionaries[i], s=100, color=colors[i])
        for key, value in points_dictionaries[i].items():
            shift = confidence_intervals[i][key] / 2.0
            plt.plot([key, key], [value-shift, value+shift], color=colors[i])
    plt.xlabel("data size")
    plt.ylabel("time")
    plt.savefig(path)
