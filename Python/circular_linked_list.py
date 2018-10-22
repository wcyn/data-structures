class CircularLinkedList(object):

    class _DataNode(object):
        def __init__(self, value=None, next_node=None):
            self._next_node = next_node
            self._value = value

    def __init__(self):
        self._size = 0
        self._tail = None

    def is_empty(self):
        return self._size == 0

    def add_element(self, value):
        if self.is_empty():
            new_node = self._DataNode(value)
            new_node._next_node = new_node
        else:
            new_node = self._DataNode(value, self._tail._next_node)
            self._tail._next_node = new_node
        self._tail = new_node
        self._size += 1

    def print_elements(self):
        if self.is_empty():
            print("There is no element in the circular linked list")
            return
        node = self._tail._next_node
        while node._next_node is not self._tail._next_node:
            print(node._value)
            node = node._next_node
        print(node._value)
        return

c_linked_list = CircularLinkedList()

# 1,2,3
c_linked_list.add_element(1)
c_linked_list.add_element(2)
c_linked_list.add_element(3)
c_linked_list.add_element(4)
c_linked_list.add_element(5)

c_linked_list.print_elements()

