class Edge:
    """
    :param first_node: первая вершина, в случае орграфа она будет началом ребра
    :param second_node: вторая вершина, в случае орграфа она будет концом ребра
    :param weight: вес ребра
    """
    def __init__(self, first_node, second_node, weight):
        self.weight = weight
        self.first_node = first_node
        self.second_node = second_node

    def __iter__(self):
        return iter((self.first_node, self.second_node))
