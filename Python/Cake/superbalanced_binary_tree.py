# https://www.interviewcake.com/question/python/balanced-binary-tree?course=fc1&section=trees-graphs
# Write a function to see if a binary tree ↴ is "superbalanced" (a new tree property we just made up).
#
# A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one.


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right =None

        def insert_left(self, value):
            self.left = BinaryTree.Node(value)
            return self.left

        def insert_right(self, value):
            self.right = BinaryTree.Node(value)
            return self.right


def is_balanced(root_node):
    if not root_node:
        return True

    depths = []
    nodes = [(root_node, 0)]

    while nodes:
        node, depth = nodes.pop()

        if not node.left and not node.right:
            # If it's a leaf node
            if depth not in depths:
                depths.append(depth)

                if len(depths) > 2 or (len(depths) == 2 and depths[0] - depths[1] > 1):
                    return False

        else:
            if node.left:
                nodes.append((node.left, depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))

    return True

b_tree = BinaryTree()
node_7 = b_tree.Node(7)
node_6 = b_tree.Node(6)
node_5 = b_tree.Node(5)
root = b_tree.Node(1)
node_2 = root.insert_left(2)
node_3 = root.insert_right(3)
node_4 = node_2.insert_left(4)
node_2.insert_right(5)
node_4.insert_left(6)
node_4.insert_right(7)

print(is_balanced(root))
