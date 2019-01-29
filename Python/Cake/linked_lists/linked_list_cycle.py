# https://www.interviewcake.com/question/python/linked-list-cycles?course=fc1&section=linked-lists
# You have a singly-linked list ↴ and want to check if it contains a cycle.
#
# A singly-linked list is built with nodes, where each node has:
#
# node.next—the next node in the list.
# node.value—the data held in the node. For example, if our linked list stores people in line at the movies,
# node.value might be the person's name.
# For example:
#
#   class LinkedListNode(object):
#
#     def __init__(self, value):
#         self.value = value
#         self.next  = None
#
# A cycle occurs when a node’s next points back to a previous node in the list.
# The linked list is no longer linear with a beginning and end—instead, it cycles through a loop of nodes.
#
# Write a function contains_cycle() that takes the first node in a
# singly-linked list and returns a boolean indicating whether the list contains a cycle.


class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')
d = LinkedListNode('D')
e = LinkedListNode('E')
f = LinkedListNode('F')
g = LinkedListNode('G')
h = LinkedListNode('H')

a.next = b
b.next = c
c.next = d
d.next = e
# e.next = f
# f.next = g
# g.next = h


def contains_cycle(node):
    if not node:
        raise Exception("Linked list does not contain any nodes")

    fast_pointer = slow_pointer = node
    while fast_pointer.next and fast_pointer.next.next:
        fast_pointer = fast_pointer.next.next
        print(fast_pointer.value)
        slow_pointer = slow_pointer.next
        if fast_pointer is slow_pointer:
            return True

    return False


print(contains_cycle(a))

# Bonus
# How would you detect the first node in the cycle?
#   - Define the first node of the cycle as the one closest to the head of the list.
# Would the program always work if the fast runner moves three steps every time the slow runner moves one step?
# What if instead of a simple linked list, you had a structure where each node could have several "next" nodes?
#   - This data structure is called a "directed graph." How would you test if your directed graph had a cycle?


