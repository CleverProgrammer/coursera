"""
Instructions: https://class.coursera.org/algorithmicthink1-004/wiki/graph_degree
Author: Rafeh Qazi
Date: 01/18/2016
Course Link: http://www.codeskulptor.org/#user41_x2qtw7LU3V_4.py
"""


EX_GRAPH0 = {
    0: set([1, 2]),
    1: set(),
    2: set()
}

EX_GRAPH1 = {
    0: set([1, 4, 5]),
    1: set([2, 6]),
    2: set([3]),
    3: set([0]),
    4: set([1]),
    5: set([2]),
    6: set()
}

EX_GRAPH2 = {
    0: set([1, 4, 5]),
    1: set([2, 6]),
    2: set([3, 7]),
    3: set([7]),
    4: set([1]),
    5: set([2]),
    6: set(),
    7: set([3]),
    8: set([1, 2]),
    9: set([0, 3, 4, 5, 6, 7])
}


def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and returns a dictionary corresponding to a complete directed graph with
    the specified number of nodes. A complete graph contains all possible edges subject to the restriction
    that self-loops are not allowed. The nodes of the graph should be numbered 0 to num_nodes - 1 when
    num_nodes is positive. Otherwise, the function returns a dictionary corresponding to the empty graph.

    :param int: num_nodes
    :return dict: all_nodes

    >>> make_complete_graph(3)
    {0: {1, 2}, 1: {0, 2}, 2: {0, 1}}
    >>> make_complete_graph(2)
    {0: {1}, 1: {0}}
    """
    all_nodes = {}
    for num in range(num_nodes):
        all_nodes[num] = set(range(num_nodes)) - {num}
    return all_nodes


def compute_in_degrees(diagraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the in-degrees for
    the nodes in the graph. The function should return a dictionary with the same set of keys (nodes)
    as digraph whose corresponding values are the number of edges whose head matches a particular node.

    :param diagraph: dict
    :return: dict

    >>> compute_in_degrees({0: {1, 2}, 1: {2}, 2: {}})
    {1: 1, 2: 2}
    """
    in_deg_counter = {}
    for key in diagraph:
        for value in diagraph[key]:
            if value not in in_deg_counter:
                in_deg_counter[value] = 1
            else:
                in_deg_counter[value] += 1
    return in_deg_counter

if __name__ == '__main__':
    import doctest
    # doctest.testmod()
    print(compute_in_degrees({0: {1, 2}, 1: {2}, 2: {}}))
    # print(make_complete_graph(3))

