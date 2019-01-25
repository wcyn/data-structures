# https://www.interviewcake.com/question/python/graph-coloring?course=fc1&section=trees-graphs
# Given an undirected graph ↴ with maximum degree ↴ D,
# find a graph coloring ↴ using at most D+1 colors.


class GraphNode:
    def __init__(self, label, neighbours=set()):
        self.label = label
        self.neighbours = neighbours
        self.color = None


a = GraphNode('a')
b = GraphNode('b', {a})
c = GraphNode('c', {b, a})

a.neighbours.add(b)
a.neighbours.add(b)
a.neighbours.add(c)
b.neighbours.add(c)

graph = [a, b, c]


def get_max_degree(graph):
    max_degree = 0
    for node in graph:
        max_degree = max(max_degree, len(node.neighbours))
    return max_degree


print(get_max_degree(graph))


def color_graph(graph):
    colors = [num for num in range(get_max_degree(graph) + 1)]
    for node in graph:
        for color in colors:
            if color not in {n.color for n in node.neighbours}:
                node.color = color
                break


print([(n.label, n.color) for n in graph])
color_graph(graph)
print([(n.label, n.color) for n in graph])



