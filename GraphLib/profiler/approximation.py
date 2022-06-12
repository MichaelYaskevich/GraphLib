from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def approximate(graph_size_array, time_results_array):
    train_X = transform_data_for_linear_model(graph_size_array)
    train_y = time_results_array
    model = LinearRegression()

    model.fit(train_X, train_y)

    segmentation = []
    for i in range(graph_size_array[0] * 10, graph_size_array[-1] * 10 + 1):
        segmentation.append(i * 0.1)
    test_X = transform_data_for_linear_model(segmentation)

    test_y = model.predict(test_X)

    return segmentation, test_y


def transform_data_for_linear_model(data):
    transformed_data = []
    for i in range(len(data)):
        transformed_data.append([data[i]])
    return PolynomialFeatures(degree=3).fit_transform(transformed_data)
