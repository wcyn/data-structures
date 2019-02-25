# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        new_head_node = ListNode(0)
        new_head_node.next = head

        def reverse_linked_list(head_node, k):
            current_node = head_node.next
            count_node = current_node
            node_count = 0
            while count_node:
                node_count += 1
                count_node = count_node.next
                if node_count == k:
                    break
            if node_count < k:
                return current_node

            node_count = 0
            while node_count < k - 1:
                next_next_node = current_node.next.next
                current_node.next.next = head_node.next
                head_node.next = current_node.next
                current_node.next = next_next_node
                node_count += 1

            return head_node

        current_node = new_head_node
        while current_node:
            current_node = reverse_linked_list(current_node, k)
            for i in range(k):
                if current_node:
                    current_node = current_node.next

        return new_head_node.next
