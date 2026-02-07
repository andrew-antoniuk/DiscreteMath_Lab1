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


g_10 = {
    'A': {'B': 4, 'C': 2, 'F': 3},
    'B': {'A': 4, 'C': 5, 'D': 10, 'E': 1},
    'C': {'A': 2, 'B': 5, 'D': 3, 'J': 4},
    'D': {'B': 10, 'C': 3, 'G': 6, 'H': 2},
    'E': {'B': 1, 'F': 5, 'I': 3},
    'F': {'A': 3, 'E': 5, 'G': 2},
    'G': {'D': 6, 'F': 2, 'H': 7},
    'H': {'D': 2, 'G': 7, 'I': 4},
    'I': {'E': 3, 'H': 4, 'J': 6},
    'J': {'C': 4, 'I': 6}
}
g_30 = {
    'A1':  {'A2': 4, 'A5': 7},
    'A2':  {'A1': 4, 'A3': 2, 'A6': 5},
    'A3':  {'A2': 2, 'A4': 6},
    'A4':  {'A3': 6, 'A8': 3},
    'A5':  {'A1': 7, 'A6': 4, 'A9': 8},
    'A6':  {'A2': 5, 'A5': 4, 'A7': 1},
    'A7':  {'A6': 1, 'A8': 2, 'A10': 6},
    'A8':  {'A4': 3, 'A7': 2},
    'A9':  {'A5': 8, 'A10': 5, 'A11': 3},
    'A10': {'A7': 6, 'A9': 5, 'A12': 4},
    'A11': {'A9': 3, 'A12': 7},
    'A12': {'A10': 4, 'A11': 7, 'A13': 2},
    'A13': {'A12': 2, 'A14': 6},
    'A14': {'A13': 6, 'A15': 3},
    'A15': {'A14': 3, 'A16': 5},
    'A16': {'A15': 5, 'A17': 1},
    'A17': {'A16': 1, 'A18': 4},
    'A18': {'A17': 4, 'A19': 6},
    'A19': {'A18': 6, 'A20': 2},
    'A20': {'A19': 2, 'A21': 7},
    'A21': {'A20': 7, 'A22': 3},
    'A22': {'A21': 3, 'A23': 5},
    'A23': {'A22': 5, 'A24': 4},
    'A24': {'A23': 4, 'A25': 6},
    'A25': {'A24': 6, 'A26': 2},
    'A26': {'A25': 2, 'A27': 5},
    'A27': {'A26': 5, 'A28': 3},
    'A28': {'A27': 3, 'A29': 4},
    'A29': {'A28': 4, 'A30': 6},
    'A30': {'A29': 6}
}
g_50 = {
    'N01': {'N02': 3, 'N05': 7},
    'N02': {'N01': 3, 'N03': 4, 'N06': 6},
    'N03': {'N02': 4, 'N04': 5},
    'N04': {'N03': 5, 'N08': 2},
    'N05': {'N01': 7, 'N06': 3, 'N09': 6},
    'N06': {'N02': 6, 'N05': 3, 'N07': 4},
    'N07': {'N06': 4, 'N08': 5, 'N10': 2},
    'N08': {'N04': 2, 'N07': 5},
    'N09': {'N05': 6, 'N10': 4, 'N11': 3},
    'N10': {'N07': 2, 'N09': 4, 'N12': 6},
    'N11': {'N09': 3, 'N12': 5},
    'N12': {'N10': 6, 'N11': 5, 'N13': 2},
    'N13': {'N12': 2, 'N14': 4},
    'N14': {'N13': 4, 'N15': 6},
    'N15': {'N14': 6, 'N16': 3},
    'N16': {'N15': 3, 'N17': 5},
    'N17': {'N16': 5, 'N18': 4},
    'N18': {'N17': 4, 'N19': 6},
    'N19': {'N18': 6, 'N20': 2},
    'N20': {'N19': 2, 'N21': 5},
    'N21': {'N20': 5, 'N22': 3},
    'N22': {'N21': 3, 'N23': 6},
    'N23': {'N22': 6, 'N24': 4},
    'N24': {'N23': 4, 'N25': 5},
    'N25': {'N24': 5, 'N26': 3},
    'N26': {'N25': 3, 'N27': 6},
    'N27': {'N26': 6, 'N28': 4},
    'N28': {'N27': 4, 'N29': 5},
    'N29': {'N28': 5, 'N30': 6},
    'N30': {'N29': 6, 'N31': 4},
    'N31': {'N30': 4, 'N32': 5},
    'N32': {'N31': 5, 'N33': 3},
    'N33': {'N32': 3, 'N34': 6},
    'N34': {'N33': 6, 'N35': 4},
    'N35': {'N34': 4, 'N36': 5},
    'N36': {'N35': 5, 'N37': 3},
    'N37': {'N36': 3, 'N38': 6},
    'N38': {'N37': 6, 'N39': 4},
    'N39': {'N38': 4, 'N40': 5},
    'N40': {'N39': 5, 'N41': 3},
    'N41': {'N40': 3, 'N42': 6},
    'N42': {'N41': 6, 'N43': 4},
    'N43': {'N42': 4, 'N44': 5},
    'N44': {'N43': 5, 'N45': 3},
    'N45': {'N44': 3, 'N46': 6},
    'N46': {'N45': 6, 'N47': 4},
    'N47': {'N46': 4, 'N48': 5},
    'N48': {'N47': 5, 'N49': 3},
    'N49': {'N48': 3, 'N50': 6},
    'N50': {'N49': 6}
}
g = {
'A': {'B': 4, 'C': 2, 'F': 3},
'B': {'A': 4, 'C': 5, 'D': 10, 'E': 1},
'C': {'A': 2, 'B': 5, 'D': 3},
'D': {'B': 10, 'C': 3, 'G': 6},
'E': {'B': 1, 'F': 5},
'F': {'A': 3, 'E': 5, 'G': 2},
'G': {'D': 6, 'F': 2},
}


# print(prim_algorithm(g_30))
# print(kruskal_algorithm(g))
# print(kruskal_algorithm(graph_50))
# print(kruskal_algorithm(g_10))
# print(transform_graph(g_50))
