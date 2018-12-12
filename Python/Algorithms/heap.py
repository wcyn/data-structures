class MinHeap(object):
    capacity = 10
    size = 0
    items = []

    def get_left_child_index(self, parent_index):
        return (2 * parent_index) + 1

    def get_right_child_index(self, parent_index):
        return (2 * parent_index) + 2

    def get_parent_index(self, child_index):
        return (child_index - 1) // 2

    def has_left_child(self, parent_index):
        return self.get_left_child_index(parent_index) < self.size

    def has_right_child(self, parent_index):
        return self.get_right_child_index(parent_index) < self.size

    def has_parent(self, child_index):
        return self.get_parent_index(child_index) >= 0

    def left_child(self, parent_index):
        return self.items[self.get_left_child_index(parent_index)]

    def right_child(self, parent_index):
        return self.items[self.get_right_child_index(parent_index)]

    def parent(self, child_index):
        return self.items[self.get_parent_index(child_index)]

    def peek(self):
        if self.size < 1:
            return None
        return self.items[0]

    def pop(self):
        if self.size < 1:
            return None
        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.items.pop()
        self.size -= 1
        self.heapify_down()
        return item

    def add(self, item):
        self.items.append(item)
        self.size += 1
        self.heapify_up()

    def heapify_up(self):
        index = self.size - 1
        while self.has_parent(index) and self.parent(index) > self.items[index]:
            # swap parent and element
            parent_index = self.get_parent_index(index)
            self.items[parent_index], self.items[index] = self.items[index], self.items[parent_index]
            index = self.get_parent_index(index)

    def heapify_down(self):
        index = 0
        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                smaller_child_index = self.get_right_child_index(index)
            if self.items[index] < self.items[smaller_child_index]:
                break
            else:
                self.items[index], self.items[smaller_child_index] = self.items[smaller_child_index], self.items[index]
                index = smaller_child_index

data = [1, 3, 6, 5, 7, 9, 2, 7, 4, 6, 8, 0]
h = MinHeap()
for item in data:
    h.add(item)
print(h.items)
print('Peek: ', h.peek())
print('Pop: ', h.pop())
print(h.items)

# heap = data.copy()
# import heapq
# heapq.heapify(heap)
# print(heap)