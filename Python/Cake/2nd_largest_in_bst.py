# https://www.interviewcake.com/question/python/second-largest-item-in-bst?course=fc1&section=trees-graphs
# Write a function to find the 2nd largest element in a binary search tree. ↴


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


# def second_largest_element(node, prev):
#     if not node:
#         return True
#
#     def is_smaller():
#         print(node.value, prev["prev"])
#         # return True
#         if node.value < prev["prev"]:
#             prev["prev"] = node.value
#             return node.value
#         prev["prev"] = node.value
#         return False
#
#     return (second_largest_element(node.right, prev) and is_smaller()
#             or second_largest_element(node.left, prev))


def find_largest_non_recursive(root):
    node = root
    while node.right:
        node = node.right
    return node.value


def find_largest(root_node):
    if root_node is None:
        raise ValueError('Tree must have at least 1 node')
    if root_node.right is not None:
        return find_largest(root_node.right)
    return root_node.value


def find_second_largest(root):
    if root is None or (root.left is None and root.right is None):
        raise ValueError("There must be at least 2 Nodes")

    if root.right is None and root.left:
        return find_largest(root)

    if root.right and root.right.left is None and root.right.right is None:
        return root.value

    return find_second_largest(root.right)


def find_second_largest_non_recursive(root):
    if root is None or (root.left is None and root.right is None):
        raise ValueError("There must be at least 2 Nodes")

    while root:
        if root.right is None and root.left:
            return find_largest_non_recursive(root)

        if root.right and root.right.left is None and root.right.right is None:
            return root.value
        root = root.right


b_tree = BinaryTree()
root = b_tree.Node(5)
node_2 = root.insert_left(2)
node_10 = root.insert_right(10)
node_2.insert_left(1)
node_2.insert_right(3)
node_10.insert_left(9)
node_10.insert_right(12)

# print(second_largest_element(root, {"prev": float('inf')}))
print(find_largest_non_recursive(root))
print(find_largest(root))
print(find_second_largest(root))
print(find_second_largest_non_recursive(root))
