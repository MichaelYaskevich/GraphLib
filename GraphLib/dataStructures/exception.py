class NegativeCycleError(RuntimeError):
    '''
    Some algorithms raise this exception when they find a negative cycle.
    '''
    pass


class CycleError(RuntimeError):
    '''
    Some algorithms raise this exception when they find a cycle.
    '''
    pass