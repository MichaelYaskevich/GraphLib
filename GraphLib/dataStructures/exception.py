class NegativeCycleError(RuntimeError):
    """
    Some algorithms raise this exception
        when they find a negative cycle.
    """
    pass


class CycleError(RuntimeError):
    """
    Some algorithms raise this exception when they find a cycle.
    """
    pass


class MissingNodeError(Exception):
    """
    You will see this exception if you try to connect nodes
        when one or both of them do not exist in this graph
    """
    pass


class MissingEdgeError(Exception):
    """
    You will see this exception if you try
        to get incident edge that doesn't exist
    """


class ExistingNodeError(Exception):
    """
    You will see this exception if you try
        to add existing node to some graph
    """
    pass


class ExistingEdgeError(Exception):
    """
    You will see this exception if you try
        to add existing edge to some graph
    """
