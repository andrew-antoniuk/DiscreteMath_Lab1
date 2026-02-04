"""
Docstring for test
"""

x = [('K', 4), ('C', 5), ('D', 10), ('O', 8), ('F', 4), ('Z', 4)]

# def compare(t):
#     """
#     Docstring for compare

#     :param t: Description
#     """
#     return t[1]


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


def kruskal_algorithm(graph: dict, visited: list = None) -> dict:

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

    if visited is None:
        visited = []


    return graph
