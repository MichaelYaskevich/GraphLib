class Edge:
    def __init__(self, first_node, second_node, weight):
        self.weight = weight
        self.first_node = first_node
        self.second_node = second_node

    def __iter__(self):
        return iter((self.first_node, self.second_node))
