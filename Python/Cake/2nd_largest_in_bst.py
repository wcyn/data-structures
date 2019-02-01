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


# def find_second_largest_non_recursive_incorrect(root):
#     if root is None or (root.left is None and root.right is None):
#         raise ValueError("There must be at least 2 Nodes")

#     while root:
#         if root.right is None and root.left:
#             return find_largest_non_recursive(root)

#         if root.right and root.right.left is None and root.right.right is None:
#             return root.value
#         root = root.right


def find_second_largest_2(root_node):
    if not root_node or (not root_node.left and not root_node.right):
        raise ValueError("Tree must have at least two nodes")

    if not root_node.right and root_node.left:
        return root_node.left.value

    largest_node = find_largest_node(root_node)
    if largest_node.left:
        return find_largest_node(largest_node.left).value
    second_largest_node = root_node

    while second_largest_node.right and second_largest_node.right.right:
        second_largest_node = second_largest_node.right

    return second_largest_node.value


def find_second_largest(root_node):
    if not root_node or (not root_node.left and not root_node.right):
        raise ValueError("Tree must have at least two nodes")

    node = root_node
    while node:
        if node.left and not node.right:
            return find_largest_non_recursive(node.left)

        if node.right and not node.right.right and not node.right.left:
                return node.value

        node = node.right


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

# Tests
import unittest

class Test(unittest.TestCase):

    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_full_tree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        right.insert_right(80)
        actual = find_second_largest(tree)
        expected = 70
        self.assertEqual(actual, expected)

    def test_largest_has_a_left_child(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        actual = find_second_largest(tree)
        expected = 60
        self.assertEqual(actual, expected)

    def test_largest_has_a_left_subtree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right_left = right.insert_left(60)
        right_left_left = right_left.insert_left(55)
        right_left.insert_right(65)
        right_left_left.insert_right(58)
        actual = find_second_largest(tree)
        expected = 65
        self.assertEqual(actual, expected)

    def test_second_largest_is_root_node(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        actual = find_second_largest(tree)
        expected = 50
        self.assertEqual(actual, expected)

    def test_descending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        actual = find_second_largest(tree)
        expected = 40
        self.assertEqual(actual, expected)

    def test_ascending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        right = tree.insert_right(60)
        right_right = right.insert_right(70)
        right_right.insert_right(80)
        actual = find_second_largest(tree)
        expected = 70
        self.assertEqual(actual, expected)

    def test_error_when_tree_has_one_node(self):
        tree = Test.BinaryTreeNode(50)
        with self.assertRaises(Exception):
           find_second_largest(tree)

    def test_error_when_tree_is_empty(self):
        with self.assertRaises(Exception):
           find_second_largest(None)


unittest.main(verbosity=2)