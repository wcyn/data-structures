# https://www.interviewcake.com/question/python/delete-node?course=fc1&section=linked-lists
# Delete a node from a singly-linked list, ↴ given only a variable pointing to that node.
#
# The input could, for example, be the variable b below:
#
# class LinkedListNode(object):
#
#     def __init__(self, value):
#         self.value = value
#         self.next  = None
#
# a = LinkedListNode('A')
# b = LinkedListNode('B')
# c = LinkedListNode('C')
#
# a.next = b
# b.next = c
#
# delete_node(b)


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c


def delete_linked_list_node(node, previous_node):
    previous_node.next = node.next
    node.next = None


def delete_linked_list_node_no_previous(node):
    if node.next:
        node.value = node.next.value
        node.next = node.next.next
    else:
        raise Exception("Can't delete the last node with this technique")

# There are two potential side-effects:
#
# Any references to the input node have now effectively been reassigned to its next node.
# In our example, we "deleted" the node assigned to the variable b, but in actuality we just gave it a new value (2)
# and a new next! If we had another pointer to b somewhere else in our code and we were assuming
# it still had its old value (8), that could cause bugs.
# If there are pointers to the input node's original next node,
# those pointers now point to a "dangling" node (a node that's no longer reachable by walking down our list).
# In our example above, c is now dangling.
# If we changed c, we'd never encounter that new value by walking down our list from the head to the tail.


def print_nodes(head):
    node = head
    while node:
        print(node.value)
        node = node.next


# print("Before delete", print_nodes(a))
# delete_linked_list_node(b, a)
# print("After delete", print_nodes(a))

print("Before delete", print_nodes(a))
delete_linked_list_node_no_previous(b)
print("After delete", print_nodes(a))




