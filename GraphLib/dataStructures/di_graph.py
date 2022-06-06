import queue


from GraphLib.dataStructures.edge import Edge
from GraphLib.dataStructures.graph import Graph


class DiGraph(Graph):
    def __init__(self):
        super().__init__()

    def add_edge(self, edge: Edge) -> None:
        start, end = edge
        if (start not in self.adjacency_lists
                or end not in self.adjacency_lists):
            raise ValueError(
                "Start node or end node aren't present in adjacency list")

        if (start, end) in self.nodes_to_edge_dict:
            raise ValueError("Such edge already exists")

        self.adjacency_lists[start].append(end)
        # flag = True
        # try:
        #     if get_cycle(self.adjacency_lists) is not None:
        #         self.adjacency_lists[start].pop()
        #         flag = False
        # except Exception:
        #     self.adjacency_lists[start].pop()
        #     flag = False
        # if flag:
        self.nodes_to_edge_dict[(start, end)] = edge


def get_cycle(adjacency_lists):
    """
    Finds cycle in graph
    :param adjacency_lists: representation of graph
    :return: cycle as list of nodes or None
    """
    prev = {}
    if len(adjacency_lists) < 2:
        return None
    q = queue.Queue()
    visited = {}
    for node in adjacency_lists.keys():
        if q.qsize() == 0:
            q.put(node)
            visited[node] = True
        else:
            visited[node] = False
    while q.qsize() != 0:
        node = q.get()
        for child in adjacency_lists[node]:
            prev[child] = node
            if visited[child]:
                return build_cycle(node, child, prev)
            else:
                q.put(child)
                visited[child] = True
    return None
