""" Descr """

import networkx

BIG = 10**9

def bellman_ford(n, edges, start):
    """
    n      — кількість вершин (0..n-1)
    edges  — список ребер (u, v, w) для u -> v з вагою w
    start  — стартова вершина

    Повертає: (dist, parent, has_negative_cycle)
    """
    dist = [BIG] * n
    parent = [-1] * n
    dist[start] = 0

    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != BIG and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True
        if not updated:
            break

    has_negative_cycle = False
    for u, v, w in edges:
        if dist[u] != BIG and dist[u] + w < dist[v]:
            has_negative_cycle = True
            break

    return dist, parent, has_negative_cycle

def get_path(parent, start, end):

    """
    Docstring for get_path

    :param parent: Description
    :param start: Description
    :param end: Description
    """

    path = []
    cur = end
    while cur != -1:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    if path[0] == start:
        return path
    return None

def nx_to_edge_list(G):
    edges = []
    for u, v, w in G.edges(data="weight"):
        edges.append((u, v, w))
        edges.append((v, u, w))  # BF usually assumes directed
    return edges

if __name__ == "__main__":
    ed = [
        (0, 1, 6),
        (0, 2, 7),
        (1, 2, 8),
        (1, 3, 5),
        (1, 4, -4),
        (2, 3, -3),
        (2, 4, 9),
        (3, 1, -2),
        (4, 3, 7),
        (4, 0, 2),
    ]

    d, p, neg = bellman_ford(5, ed, 0)

    # print("dist:", d)
    # print("parent:", p)
    # print("negative cycle:", neg)
    # print(get_path(p, 0, 3))
