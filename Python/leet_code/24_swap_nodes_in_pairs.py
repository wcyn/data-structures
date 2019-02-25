# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


head_node = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
head_node.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head and head.next:
            next_next_node = head.next.next
            new_head = head.next
            new_head.next = head
            head.next = next_next_node
        else:
            return head

        def node_swap(current_node, previous_node):
            while current_node and current_node.next:
                next_next_node = current_node.next.next
                swap_node = current_node.next
                swap_node.next = current_node
                previous_node.next = swap_node
                previous_node = current_node
                current_node.next = next_next_node
                current_node = next_next_node

        previous_node = head
        current_node = head.next
        node_swap(current_node, previous_node)
        # while current_node and current_node.next:
        #     next_next_node = current_node.next.next
        #     swap_node = current_node.next
        #     swap_node.next = current_node
        #     previous_node.next = swap_node
        #     previous_node = current_node
        #     current_node.next = next_next_node
        #     current_node = next_next_node

        return new_head


sol = Solution()

head_node = sol.swapPairs(head_node)

while head_node:
    print(head_node.val)
    head_node = head_node.next

