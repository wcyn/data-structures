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

    def add_edge(self, source, destination):
        s = self.get_node(source)
        d = self.get_node(destination)
        if s and d:
            s.adjacent.append(d)

    def has_path_DFS(self, source, destination):
        s = self.get_node(source)
        d = self.get_node(destination)
        visited = set()

        return self._has_path_DFS(s, d, visited)

    def _has_path_DFS(self, source, destination, visited):
        print(f's: {source.name}, d:{destination.name}')
        if source.name in visited:
            return False

        if source is destination:
            return True

        visited.add(source.name)
        for child in source.adjacent:
            return self._has_path_DFS(child, destination, visited)

        return False

g = Graph()
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_node('F')

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('A', 'D')
g.add_edge('B', 'E')
g.add_edge('D', 'E')
g.add_edge('E', 'F')

print(g.has_path_DFS('B', 'D'))