class LinkedList(object):
    head = None
    class Node(object):
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def add(self, value):
        new_node = self.Node(value)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def print_nodes(self):
        current_node = self.head
        while current_node:
            print(current_node.value.name)
            current_node = current_node.next

# l_list = LinkedList()
# l_list.add('A')
# l_list.add('B')
# l_list.add('C')
# l_list.print_nodes()

class Graph(object):
    nodes = {}

    class Node(object):
        def __init__(self, name):
            self.name = name
            self.adjacent = LinkedList()

    def add_node(self, name):
        self.nodes[name] = self.Node(name)

    def get_node(self, name):
        return self.nodes.get(name)

    def add_edge(self, source, destination):
        s = self.get_node(source)
        d = self.get_node(destination)
        if s and d:
            s.adjacent.add(d)

    def has_path_DFS(self, source, destination):
        s = self.get_node(source)
        d = self.get_node(destination)
        print(f's: {s.name}, d:{d.name}')
        visited = set()
        return self._has_path_DFS(s, d, visited)

    def _has_path_DFS(self, source, destination, visited):
        print(f'source: {source.name}, dest:{destination.name}')
        if source.name in visited:
            return False
        visited.add(source.name)
        if source == destination:
            return True

        current = source.adjacent.head
        # source.adjacent.print_nodes()
        while current:
            print(f'current: {current.value.name}')
            if self._has_path_DFS(current.value, destination, visited):
                return True
            current = current.next
        return False

graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('C', 'E')
graph.add_edge('B', 'D')
graph.add_edge('D', 'E')
graph.add_edge('D', 'F')
graph.add_edge('E', 'F')

# print(graph.get_node('A').adjacent)
# print(graph.get_node('B').adjacent)
# graph.get_node('D').adjacent.print_nodes()
print(graph.has_path_DFS('D', 'A'))