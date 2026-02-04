"""
Docstring for algo
"""

def get_smallest_edge(graph: dict) -> tuple[str, tuple[str, int]]:

    """
    Docstring for smallest_edge

    :param graph: Description
    :type graph: dict
    :return: Description
    :rtype: tuple[str, tuple[str, int]]
    """

    def compare_1(t):
        return t[1]

    def compare_2(t):
        return t[1][1]

    return min(((k, min(graph[k], key = compare_1)) for k in graph), key = compare_2)


def kruskal_algorithm(graph: dict) -> dict:

    """
    Docstring for kruskal_algo

    :param graph: Description
    :type graph: dict
    :return: Description
    :rtype: dict

    graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 5), ('D', 10)],
    'C': [('A', 2), ('B', 5), ('D', 3)],
    'D': [('B', 10), ('C', 3)]
    """

    def compare(t):
        return t[1]

    min(graph.items(), key = compare)


def prim_algorithm(graph: dict) -> dict:

    """
    Docstring for prim_algorithm

    graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 5), ('D', 10)],
    'C': [('A', 2), ('B', 5), ('D', 3)],
    'D': [('B', 10), ('C', 3)]
    }

    :param graph: Description
    :type graph: dict
    :return: Description
    :rtype: dict
    """

    def compare(t):
        return t[1]

    d = {}
    current = min(graph.keys())
    visited = [current]

    while len(d) != len(graph):

        n = [item for item in graph[current] if item[0] not in visited]

        if not n:
            continue

        v, w = min(n, key = compare)
        d[(current, v)] = w
        current = v
        visited.append(current)

    return d


g = {
'A': [('B', 4), ('C', 2)],
'B': [('A', 4), ('C', 5), ('D', 10)],
'C': [('A', 2), ('B', 5), ('D', 3)],
'D': [('B', 10), ('C', 3)]
}

# print(prim_algorithm(g))
