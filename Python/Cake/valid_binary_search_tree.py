# Write a function to check that a binary tree ↴ is a valid binary search tree. ↴
# A binary search tree is a binary tree in which, for each node:
#
# The node's value is greater than all values in the left subtree.
# The node's value is less than all values in the right subtree.
# BSTs are useful for quick lookups. If the tree is balanced,
# we can search for a given value in the tree in O(lg(n))O(lg(n)) time.
import collections


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.low = float('-inf')
            self.high = float('inf')

        def insert_left(self, value):
            self.left = BinaryTree.Node(value)
            return self.left

        def insert_right(self, value):
            self.right = BinaryTree.Node(value)
            return self.right


def is_valid_binary_tree_breadth_first(root_node):
    nodes = collections.deque([root_node])
    while nodes:
        current_node = nodes.popleft()
        print(current_node.value)
        if current_node.left:
            if not child_valid(current_node.left, current_node.low, current_node.value):
                return False
            nodes.append(current_node.left)
        if current_node.right:
            if not child_valid(current_node.right, current_node.value, current_node.high):
                return False
            nodes.append(current_node.right)
    return True


def is_valid_binary_tree_depth_first(root_node):
    nodes = [root_node]
    while nodes:
        current_node = nodes.pop()
        print(current_node.value)
        if current_node.right:
            if not node_valid(current_node.right, current_node.value, current_node.high):
                return False
            nodes.append(current_node.right)
        if current_node.left:
            if not node_valid(current_node.left, current_node.low, current_node.value):
                return False
            nodes.append(current_node.left)

    return True


def node_valid(node, lowest, highest):
    if node:
        node.low = lowest
        node.high = highest
        if lowest <= node.value <= highest:
            return True
        return False
    return False


#  Cake solution
def is_binary_search_tree(root):
    # Start at the root, with an arbitrarily low lower bound
    # and an arbitrarily high upper bound
    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    # Depth-first traversal
    while len(node_and_bounds_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        # If this node is invalid, we return false right away
        if (node.value <= lower_bound) or (node.value >= upper_bound):
            return False

        if node.left:
            # This node must be less than the current node
            node_and_bounds_stack.append((node.left, lower_bound, node.value))
        if node.right:
            # This node must be greater than the current node
            node_and_bounds_stack.append((node.right, node.value, upper_bound))

    # If none of the nodes were invalid, return true
    # (at this point we have checked all nodes)
    return True


def is_binary_search_tree_recursive(node, low, high):
    # nodes = [(root, float('-inf'), float('inf'))]
    # print(node.value, low, high)
    if not node:
        return True
    if not node_valid(node, low, high):
        return False
    return (is_binary_search_tree_recursive(node.left, low, node.value)
            and is_binary_search_tree_recursive(node.right, node.value, high))

#  Checking if an in-order traversal of the tree is sorted is a great answer too,
# especially if you're able to implement it without storing a full list of nodes.

b_tree = BinaryTree()
root = b_tree.Node(5)
node_2 = root.insert_left(2)
node_10 = root.insert_right(10)
node_2.insert_left(1)
node_2.insert_right(3)
node_10.insert_left(10)
node_10.insert_right(12)

# print(is_valid_binary_tree_breadth_first(root))
# print(is_valid_binary_tree_depth_first(root))
# print(is_binary_search_tree_recursive(root, float('-inf'), float('inf')))


def in_order_traversal(node, prev):
    if not node:
        return True

    def is_valid():
        print(node.value, prev['prev'])
        if node.value >= prev['prev']:
            prev['prev'] = node.value
            return True
        prev['prev'] = node.value
        return False

    return (in_order_traversal(node.left, prev) and is_valid() and
            in_order_traversal(node.right, prev)
            )


print(in_order_traversal(root, {"prev": float('-inf')}))

