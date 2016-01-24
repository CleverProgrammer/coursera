"""
Instructions: https://class.coursera.org/algorithmicthink1-004/wiki/graph_degree
Author: Rafeh Qazi
Date: 01/18/2016
Course Link: http://www.codeskulptor.org/#user41_x2qtw7LU3V_8.py
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
    :return in_deg_counter: dict

    >>> compute_in_degrees({0: {1, 2}, 1: {2}, 2: {}})
    {0: 0, 1: 1, 2: 2}
    """
    in_deg_counter = {}
    for values in diagraph.values():
        for value in values:
            if value not in in_deg_counter:
                in_deg_counter[value] = 1
            else:
                in_deg_counter[value] += 1

    # Set node in degrees to 0 if they have no in degrees.
    for key in diagraph:
        if key not in in_deg_counter:
            in_deg_counter[key] = 0

    return in_deg_counter


def in_degree_distribution(diagraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the unnormalized
    distribution of the in-degrees of the graph. The function should return a dictionary
    whose keys correspond to in-degrees of nodes in the graph. The value associated with each
    particular in-degree is the number of nodes with that in-degree. In-degrees with no corresponding
    nodes in the graph are not included in the dictionary

    :param diagraph: dict
    :return in_degree_dist: dict

    >>> in_degree_distribution({0: {1, 2}, 1: {1}, 2: {}})
    {0: 1, 1: 1, 2: 1}
    """
    node_in_degrees = compute_in_degrees(diagraph)
    in_degree_dist = {}
    for in_degree in node_in_degrees.values():
        if in_degree not in in_degree_dist:
            in_degree_dist[in_degree] = 1
        else:
            in_degree_dist[in_degree] += 1
    return in_degree_dist


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(compute_in_degrees({0: {1, 2}, 1: {2}, 2: {}}))
    # print(make_complete_graph(3))
