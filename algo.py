"""
Algorithms & Testing Field
"""

def kruskal_algorithm(graph: dict[str, dict[str, int]]) -> dict[str, dict[str, int]]:

    """
    Kruskal's Algorithm for finding minimum spanning tree of given weighted graph.
    The main concept of this algorithm is to choose edge with the least possible weight
    at each step in the whole graph, so that no cycle can be formed,
    and repeat thos process until no unvisited nodes left.

    In this functional implementation
    we first transform the graph into more practial form of data,
    which follows this structure:
    [('A', 'B', d), ...], where 'A' and 'B' are nodes and 'd' is numerical distance

    Then we start iterance over brand new sorted data and fill 'tree' placeholder with values,
    when we meet the belong condition

    Works only for similar graph representation below:

    g = {
    'A': {'B': 4, 'C': 2, 'D': 3},
    'B': {'A': 4},
    'C': {'A': 2, 'D': 2},
    'D': {'A': 3, 'C': 2, 'D': 3},
    }

    :param graph: Given graph to get MST
    :type graph: dict[str, dict[str, int]]
    :return dict[str, dict[str, int]]: Minimum spanning tree of the graph
    """

    edges = []
    visited = set()
    for u in graph: # transform graph into [('A', 'B', d), ...]
        for v, w in graph[u].items():
            if (v, u) not in visited:
                edges.append((u, v, w))
                visited.add((u, v))

    f = [{node} for node in graph] # for iteration
    tree = {node: {} for node in graph} # result

    for u, v, w in sorted(edges, key = lambda x: x[2]):
        # Find which sets u and v belong to
        u_iter = next(s for s in f if u in s)
        v_iter = next(s for s in f if v in s)

        if u_iter != v_iter: # difference check
            tree[u][v] = w
            tree[v][u] = w

            u_iter.update(v_iter)
            f.remove(v_iter)

        if len(f) == 1: # loop end at n-1 iteration
            break

    return tree


def prim_algorithm(graph: dict[str, dict[str, int]], start = None) -> dict[str, dict[str, int]]:

    """
    Prim's Algorithm for finding minimum spanning tree of given weighted graph.
    The main concept of this algorithm is to start from any node you want
    and choose edge with the least possible weight
    at each step from neighboring nodes, so that no cycle can be formed,
    and repeat thos process until no unvisited nodes left.

    In this functional implementation
    we first choose the starting point
    then we look at neighboring nodes and choose the least weighted one to go there,
    so that no cycle can be formed or visited nodes can be visited.

    Works only for similar graph representation below:

    g = {
    'A': {'B': 4, 'C': 2, 'D': 3},
    'B': {'A': 4},
    'C': {'A': 2, 'D': 2},
    'D': {'A': 3, 'C': 2, 'D': 3},
    }
    """

    if start is None: # in case of no user-input
        start = min(graph.keys())

    lenght = len(graph) # no need to call len() every time
    visited = {start}
    tree = {v: {} for v in graph} # placeholder

    while len(visited) < lenght: # stop condition

        # iteration over edges for min-weight
        u, v, w = min((u, v, w) for u in visited for v, w in graph[u].items() if v not in visited)

        # save result
        tree[u][v] = w
        tree[v][u] = w
        visited.add(v)

    return tree
