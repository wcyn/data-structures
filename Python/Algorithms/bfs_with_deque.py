from collections import deque

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
        source_node = self.get_node(source)
        dest_node = self.get_node(destination)

        if source_node and dest_node:
            source_node.adjacent.append(dest_node)

    def has_path_BFS(self, source, destination):
        next_to_visit = deque()
        visited = set()

        source_node = self.get_node(source)
        dest_node = self.get_node(destination)
        next_to_visit.append(source_node)

        # print(f'Next 2 visit: {[n.name for n in next_to_visit]}, Source Node: {source_node.name}, Dest Node: {dest_node.name}')

        while next_to_visit:
            print(f'Next 2 visit: {[n.name for n in next_to_visit]}, Source Node: {source_node.name}, Dest Node: {dest_node.name}, visited: {visited}')
            node = next_to_visit.popleft()
            print(f'node: {node.name}')
            if node is dest_node:
                return True
            if node.name in visited:
                continue
            visited.add(node.name)
            # print(f'Adj: {node.adjacent}')
            for child in node.adjacent:
                next_to_visit.append(child)

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
g.add_edge('C', 'E')
g.add_edge('B', 'D')
g.add_edge('D', 'E')
g.add_edge('D', 'F')
g.add_edge('E', 'F')

# print(g.nodes.get('A'))
# print(g.get_node('A'))

print(g.has_path_BFS('A', 'F'))
