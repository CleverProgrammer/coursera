# http://matthiaseisen.com/articles/graphviz/
import graphviz as gv


# Draw a graph whose adjacency matrix is
#      A B C D
# A   [0 1 1 0]
# B   [1 0 0 1]
# C   [1 0 0 1]
# D   [0 1 1 0]

g1 = gv.Graph(format='svg')

# Create nodes A, B, C, D
for nodde in ['A', 'B', 'C', 'D']:
    g1.node(nodde)

# Create the edges based on the adjacency matrix
g1.edge('A', 'B')
g1.edge('A', 'C')
g1.edge('B', 'A')
g1.edge('B', 'D')
g1.edge('C', 'A')
g1.edge('C', 'D')
g1.edge('D', 'B')
g1.edge('D', 'C')

# Create the graph file and save it
graph = g1.render(filename='img/g1')
print(graph)
