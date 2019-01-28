# https://www.interviewcake.com/question/python/largest-stack?course=fc1&section=queues-stacks
# You want to be able to access the largest element in a stack. ↴
# You've already implemented this Stack class:
# Use your Stack class to implement a new class MaxStack with a method get_max()
# that returns the largest element in the stack. get_max() should not remove the item.
# Your stacks will contain only integers.


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(Stack):

    def __init__(self):
        super().__init__()
        self.max_num = float('-inf')

    def push(self, item):
        if not self.items:
            self.items.append((item, item))
            return
        _, current_max = self.peek()
        self.items.append((item, max(current_max, item)))

    def get_max_expensive(self):
        if not self.items:
            return None

        popped_nums = []
        while self.items:
            popped_nums.append(self.pop())
            if popped_nums[-1] > self.max_num:
                self.max_num = popped_nums[-1]

        while popped_nums:
            self.push(popped_nums.pop())
        print(self.items)
        return self.max_num

    def get_max(self):
        if not self.items:
            return None
        return self.peek()[1]


class MaxStack2(object):

    def __init__(self):
        self.stack = Stack()
        self.maxes_stack = Stack()

    def push(self, item):
        """Add a new item onto the top of our stack."""
        self.stack.push(item)

        # If the item is greater than or equal to the last item in maxes_stack,
        # it's the new max! So we'll add it to maxes_stack.
        if self.maxes_stack.peek() is None or item >= self.maxes_stack.peek():
            self.maxes_stack.push(item)

    def pop(self):
        """Remove and return the top item from our stack."""
        item = self.stack.pop()

        # If it equals the top item in maxes_stack, they must have been pushed
        # in together. So we'll pop it out of maxes_stack too.
        if item == self.maxes_stack.peek():
            self.maxes_stack.pop()

        return item

    def get_max(self):
        """The last item in maxes_stack is the max item in our stack."""
        return self.maxes_stack.peek()


m_stack = MaxStack2()
m_stack.push(11)
m_stack.push(2)
m_stack.push(15)
m_stack.push(1)
m_stack.push(17)
m_stack.push(9)
m_stack.push(17)
m_stack.push(15)
print(m_stack.get_max())
print("Pop:", m_stack.pop())
print(m_stack.get_max())
print("Pop:", m_stack.pop())
print(m_stack.get_max())
print("Pop:", m_stack.pop())
print(m_stack.get_max())
print("Pop:", m_stack.pop())
print(m_stack.get_max())
print("Pop:", m_stack.pop())
print(m_stack.get_max())
print("Pop:", m_stack.pop())
print(m_stack.get_max())
