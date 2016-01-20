def graph(current_nodes):
    """
    >>> graph(4)
    6
    >>> graph(5)
    10
    >>> graph(10)
    45
    """
    # Multiplying by an even and odd number
    # guaranteed that the product will be an even number.
    return ((current_nodes - 1) * (current_nodes)) // 2

    # Recursive case
    # if not current_nodes:
    #     return 0
    # return (current_nodes - 1) + graph(current_nodes - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
