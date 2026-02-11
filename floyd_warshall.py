""" Descr """

import networkx

INF = 10**9

def print_matrix(matrix, k):

    """
    Docstring for print_matrix

    :param matrix: Description
    :param k: Description
    """

    print(f"\nW^{k}:")
    for row in matrix:
        for val in row:
            if val == INF:
                print("∞".rjust(4), end=" ")
            else:
                print(str(val).rjust(4), end=" ")
        print()

def floyd_warshall(graph):

    """
    Docstring for floyd_warshall

    :param graph: Description
    """

    n = len(graph)
    dist = [row[:] for row in graph]

    # print("Початкова матриця:")
    # print_matrix(dist, 0)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

        # print_matrix(dist, k + 1)

    return dist

g = [
    [0,    5,    INF, 10],
    [INF,  0,    3,   INF],
    [INF,  INF,  0,   1],
    [INF,  INF,  INF, 0]
]

floyd_warshall(g)

INF = float("inf")

def nx_to_adj_matrix(G):
    nodes = list(G.nodes())
    idx = {node: i for i, node in enumerate(nodes)}
    n = len(nodes)

    matrix = [[INF]*n for _ in range(n)]
    for i in range(n):
        matrix[i][i] = 0

    for u, v, w in G.edges(data="weight"):
        i, j = idx[u], idx[v]
        matrix[i][j] = w
        matrix[j][i] = w  # undirected

    return matrix
