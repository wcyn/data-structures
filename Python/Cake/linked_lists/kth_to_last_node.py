# https://www.interviewcake.com/question/python/kth-to-last-node-in-singly-linked-list?course=fc1&section=linked-lists
# You have a linked list ↴ and want to find the kth to last node.
#
# Write a function kth_to_last_node() that takes an integer k and the head_node of a singly-linked list,
# and returns the kth to last node in the list.

from collections import deque


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next  = None


a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e


def get_kth_to_last_node_k_space(k, head_node):
    last_k_nodes = deque()
    node = head_node
    while node:
        if len(last_k_nodes) == k:
            last_k_nodes.popleft()
        last_k_nodes.append(node)
        node = node.next

    if len(last_k_nodes) < k:
        raise Exception("There are less than {} nodes in the linked list".format(k))
    return last_k_nodes[0]


def get_kth_to_last_node_constant_space(k, head_node):
    # Count number of nodes
    node_count = 0
    node = head_node
    while node:
        node_count += 1
        node = node.next

    if node_count < k:
        raise Exception("There are less than {} nodes in the linked list".format(k))

    kth_position = node_count - k
    node_index = 0
    node = head_node
    while node_index < kth_position:
        node = node.next
        node_index += 1

    return node


def get_kth_to_last_node_constant_space_best(k, head_node):
    right_node = left_node = head_node

    for _ in range(k-1):
        if not right_node:
            raise Exception("There are less than {} nodes in the linked list".format(k))
        right_node = right_node.next

    print(right_node.value)
    while right_node.next:
        right_node = right_node.next
        left_node = left_node.next

    return left_node


print(get_kth_to_last_node_k_space(2, a).value)
print(get_kth_to_last_node_constant_space(2, a).value)
print(get_kth_to_last_node_constant_space_best(2, a).value)

# What We Learned
# We listed two good solutions. One seemed to solve the problem in one pass,
# while the other took two passes. But the single-pass approach didn't take half as many steps,
# it just took the same steps in a different order.
#
# So don't be fooled: "one pass" isn't always fewer steps than "two passes."
# Always ask yourself, "Have I actually changed the number of steps?"

