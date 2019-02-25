"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

https://leetcode.com/problems/merge-two-sorted-lists/

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node_pointer_1 = l1
        node_pointer_2 = l2
        sorted_list_head = ListNode(0)
        sorted_list_tail = sorted_list_head

        while node_pointer_1 and node_pointer_2:
            if node_pointer_1.val < node_pointer_2.val:
                sorted_list_tail.next = node_pointer_1
                sorted_list_tail = sorted_list_tail.next
                node_pointer_1 = node_pointer_1.next
            else:
                sorted_list_tail.next = node_pointer_2
                sorted_list_tail = sorted_list_tail.next
                node_pointer_2 = node_pointer_2.next
        sorted_list_tail.next = node_pointer_1 or node_pointer_2

        return sorted_list_head.next

