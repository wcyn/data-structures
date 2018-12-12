class Graph(object):
    nodes = {}
    class Node(object):
        def __init__(self, name):
            self.name = name
            self.adjacent = []

    def add_node(self, name):
        self.nodes[name] = self.Node(name)

    def get_node(self, name):
        return self.nodes.get(name)

    def add_edge(self, name):
        return