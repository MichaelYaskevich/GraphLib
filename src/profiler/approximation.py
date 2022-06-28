from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def approximate(graph_size_array, time_results_array):
    """
    Создает аппроксимирующую функцию.

    :param graph_size_array: размеры графов
    :param time_results_array: результаты для каждого размера
    :return: координаты по x и y для графика аппроксимирующей функции
    """

    train_X = transform_data_for_linear_model(graph_size_array)
    train_y = time_results_array
    model = LinearRegression()

    model.fit(train_X, train_y)

    result_x = []
    for i in range(graph_size_array[0] * 10, graph_size_array[-1] * 10 + 1):
        result_x.append(i * 0.1)
    test_X = transform_data_for_linear_model(result_x)

    result_y = model.predict(test_X)

    return result_x, result_y


def transform_data_for_linear_model(data, n=3):
    """
    Превращает одномерный вектор в n-мерный для того, чтобы
    приблизить полиномиальную функцию кусочно-линейной функцией.

    :param data: одномерный вектор
    :param n: степень полиномиальной функции
    :return: n-мерный вектор
    """

    transformed_data = []
    for i in range(len(data)):
        transformed_data.append([data[i]])
    return PolynomialFeatures(degree=n).fit_transform(transformed_data)
