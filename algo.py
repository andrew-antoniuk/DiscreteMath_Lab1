"""
Algorithms & Testing Field
"""

import networkx

def nx_to_adj_dict(G):

    """
    Docstring for nx_to_adj_dict

    :param G: Description
    """

    adj = {}
    for u in G.nodes():
        adj[u] = {}
    for u, v, w in G.edges(data="weight"):
        adj[u][v] = w
        adj[v][u] = w
    return adj

def kruskal_algorithm(graph: dict[str, dict[str, int]]) -> dict[str, dict[str, int]]:

    """
    Kruskal's Algorithm for finding minimum spanning tree of given weighted graph.
    The main concept of this algorithm is to choose edge with the least possible weight
    at each step in the whole graph, so that no cycle can be formed,
    and repeat thos process until no unvisited nodes left.

    Then we start iterance over brand new sorted data and fill 'tree' placeholder with values,
    when we meet the belong condition
    Works only for similar graph representation below:

    g = {
    'A': {'B': 4, 'C': 2, 'D': 3},
    'B': {'A': 4},
    'C': {'A': 2, 'D': 2},
    'D': {'A': 3, 'C': 2, 'D': 3},
    }
    """

    edges = sorted([(w, v, u) for u in graph for v, w in graph[u].items() if u < v])

    f = [{n} for n in graph]
    tree = {n: {} for n in graph}

    for w, v, u in edges:
        u_it = next(c for c in f if u in c)
        v_it = next(c for c in f if v in c)

        if u_it != v_it:
            tree[u][v] = w
            tree[v][u] = w

            u_it.update(v_it)
            f.remove(v_it)

        if len(f) == 1:
            return tree


def prim_algorithm(graph: dict[str, dict[str, int]]) -> dict[str, dict[str, int]]:

    """
    Prim's Algorithm for finding minimum spanning tree of given weighted graph.
    The main concept of this algorithm is to start from the lightest edge
    and choose neighboring edges with the least possible weight
    at each steps, so that no cycle can be formed,
    and repeat this process until no unvisited nodes left.
    Works only for similar graph representation below:

    g = {
    'A': {'B': 4, 'C': 2, 'D': 3},
    'B': {'A': 4},
    'C': {'A': 2, 'D': 2},
    'D': {'A': 3, 'C': 2, 'D': 3},
    }
    """

    # choose min-weight edge
    w0, v0, u0 = min(
        (w, v, u)
        for u in graph
        for v, w in graph[u].items()
    )

    # use of the min edge
    l = len(graph)
    visited = {u0, v0}
    tree = {v: {} for v in graph}
    tree[u0][v0] = w0
    tree[v0][u0] = w0

    while len(visited) < l: # algorithm core
        # choosing the smallest one
        w, u, v = min(
            (w, u, v)
            for u in visited
            for w, v in graph[u].items()
            if w not in visited)

        tree[u][v] = w
        tree[v][u] = w
        visited.add(v)

    return tree
