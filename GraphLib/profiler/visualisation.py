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


# TODO: сделать путь не абсолютным
# TODO: научится рисовать точки на графиках и вертикальные линии
def visualize(dictionaries: list, labels: list, path):
    plt.figure(figsize=(16, 6))
    plt.title("Time performance research")
    for i in range(len(dictionaries)):
        sns.lineplot(data=dictionaries[i], label=labels[i])
    plt.xlabel("data size")
    plt.ylabel("time")
    plt.savefig(path)
