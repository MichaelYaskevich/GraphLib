#TODO: docstrings а русском
class NegativeCycleError(RuntimeError):
    """
    Некоторые алгоритмы вызывают это исключение
        когда они находят отрицательный цикл.
    """
    pass


class CycleError(RuntimeError):
    """
    Некоторые алгоритмы поднимают это исключение, когда находят цикл.
    """
    pass


class FileInWrongFormatError(RuntimeError):
    """
    Парсер вызывает это исключение, когда не может прочитать файл с графом
    """
    pass


class MissingNodeError(Exception):
    """
    Вы увидите это исключение, если попытаетесь соединить узлы
        когда один из них или оба не существуют в данном графе
    """
    pass


class MissingEdgeError(Exception):
    """
    Вы увидите это исключение, если попытаетесь
        получить несуществующую грань инцидента
    """


class ExistingNodeError(Exception):
    """
    Вы увидите это исключение, если попытаетесь
        добавить существующий узел к некоторому графу
    """
    pass


class ExistingEdgeError(Exception):
    """
    You will see this exception if you try
        to add existing edge to some graph
    """
