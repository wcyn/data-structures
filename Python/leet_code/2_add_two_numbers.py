# https://leetcode.com/problems/add-two-numbers/
class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        place = 10

        val1 = val2 = val3 = 0
        start_node = self.ListNode(None)
        current_node = start_node
        while True:
            val1 = val2 = 0
            if l1: val1 = l1.val
            if l2: val2 = l2.val

            n_sum = carry + val1 + val2
            if n_sum > 9:
                carry = 1
                val3 = n_sum - 10
            else:
                carry = 0
                val3 = n_sum
            if l1: l1 = l1.next
            if l2: l2 = l2.next

            new_node = self.ListNode(val3)
            current_node.next = new_node
            current_node = new_node
            if l1 is None and l2 is None:
                if carry == 1:
                    new_node = self.ListNode(carry)
                    current_node.next = new_node
                return start_node.next

# Create Nodes
def create_linked_list(num_list):
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    start_node = ListNode(None)
    current_node = start_node
    for num in num_list:
        new_node = ListNode(num)
        current_node.next = new_node
        current_node = new_node
    return start_node.next

sol = Solution()
l1 = create_linked_list([2,4,3])
l2 = create_linked_list([5,6,4])

def get_result():
    result = []
    linked_list = sol.addTwoNumbers(l1, l2)
    while True:
        if linked_list: result.append(linked_list.val)
        else: return result
        linked_list = linked_list.next

print(get_result())