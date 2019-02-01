# https://www.interviewcake.com/question/python/reverse-linked-list?course=fc1&section=linked-lists
# Hooray! It's opposite day. Linked lists go the opposite way today.
#
# Write a function for reversing a linked list. ↴ Do it in place. ↴
#
# Your function will have one input: the head of the list.
#
# Your function should return the new head of the list.

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
e.next = f
f.next = g
# g.next = h


def reverse_linked_list(head_node):
    if not head_node:
        raise Exception("Linked List has no nodes")

    if not head_node.next:
        return head_node

    previous_node = None
    current_node = head_node
    next_node = head_node.next

    while next_node:
        if next_node.next:
            temp_node = next_node.next
        else:
            temp_node = None
        next_node.next = current_node
        current_node.next = previous_node
        previous_node = next_node
        current_node = temp_node
        if current_node:
            next_node = current_node.next
        else:
            next_node = None

    if current_node:
        return current_node
    return previous_node


def reverse_linked_list_that_works_for_even_and_odd_number_of_nodes(head_node):
    if not head_node:
        return None

    if not head_node.next:
        return head_node

    previous_node = None
    current_node = head_node

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node

        previous_node = current_node
        current_node = next_node

    return previous_node


def print_nodes(head):
    node = head
    while node:
        print(node.value)
        node = node.next


print("Before reverse: ")
print_nodes(a)
new_head_node = reverse_linked_list_that_works_for_even_and_odd_number_of_nodes(a)
# print(new_head_node.value)
print("\n\nAfter reverse: ")
print_nodes(new_head_node)

# Bonus
# This in-place ↴ reversal destroys the input linked list.
# What if we wanted to keep a copy of the original linked list?
# Write a function for reversing a linked list out-of-place.


