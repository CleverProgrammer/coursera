# Instructions: https://class.coursera.org/algorithmicthink1-004/wiki/graph_degree
# Author: Rafeh Qazi
# Date: 01/18/2016

import itertools


EX_GRAPH0 = {
    0: {1, 2},
    1: {},
    2: {}
}

EX_GRAPH1 = {
    0: {1, 4, 5},
    1: {2, 6},
    2: {3},
    3: {0},
    4: {1},
    5: {2},
    6: {}
}

EX_GRAPH2 = {
    0: {1, 4, 5},
    1: {2, 6},
    2: {3, 7},
    3: {7, 9},
    4: {1},
    5: {2},
    6: {},
    7: {3},
    8: {1, 2},
    9: {0, 3, 4, 5, 6, 7}
}


def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and returns a dictionary corresponding to a complete directed graph with
    the specified number of nodes. A complete graph contains all possible edges subject to the restriction
    that self-loops are not allowed. The nodes of the graph should be numbered 0 to num_nodes - 1 when
    num_nodes is positive. Otherwise, the function returns a dictionary corresponding to the empty graph.

    :param num_nodes: int
    :return: dict
    """
    max_edges = (num_nodes * (num_nodes - 1)) // 2
    combos = list(itertools.combinations(range(num_nodes), 2))
    all_nodes = {}
    range_ = range(num_nodes)
    for combo in combos:
        if combo[0] not in all_nodes:
            all_nodes[combo[0]] = {combo[1]}
        else:
            all_nodes[combo[0]].add(combo[1])

    # Figure out the range to set to 0 nodes.
    for i in range_:
        if i not in all_nodes:
            range_ = range(i, num_nodes)
            break

    # Assign that range to 0 nodes or an empty set.
    for i in range_:
        all_nodes[i] = {}
    return all_nodes


def playground():
    x = list(itertools.combinations(['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8'], 2))
    max_edges = (8 * (8 - 1)) // 2
    print(max_edges)
    print(len(x))
    a = {}
    key = "somekey"
    a.setdefault(key, [])
    a[key].append(1)
    print(x)


if __name__ == '__main__':
    print(make_complete_graph(8))
    print(make_complete_graph(3))
