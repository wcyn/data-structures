# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Queue import PriorityQueue


class Solution(object):
    def mergeKLists1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        if not lists:
            return []

        merge_list = ListNode(0)
        current_merge_node = merge_list

        current_nodes = [node for node in lists if node]

        if not current_nodes:
            return []

        while True:
            min_value_node = (float('inf'), None, None)
            for index, node in enumerate(current_nodes):
                if node:
                    min_value_node = min(min_value_node, (node.val, node, index))
            if min_value_node[1] is None:
                break
            current_merge_node.next = min_value_node[1]
            current_merge_node = current_merge_node.next
            current_nodes[min_value_node[2]] = current_nodes[min_value_node[2]].next
        return merge_list.next

    def mergeKLists2(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

    def mergeKLists3(self, lists):
        head = current_node = ListNode(0)
        p_queue = PriorityQueue()
        for l in lists:
            if l:
                p_queue.put((l.val, l))
        while not p_queue.empty():
            value, node = p_queue.get()
            current_node.next = node
            current_node = current_node.next
            node = node.next
            if node:
                p_queue.put((node.val, node))
        return head.next

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next

