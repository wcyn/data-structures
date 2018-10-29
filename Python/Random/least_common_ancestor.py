class BinaryNode(object):
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

def path_from_root(node):
    path = []
    while node:
        path.insert(0, node)
        node = node.parent
    return path

def lca_with_parent(node1, node2):
    path1 = path_from_root(node1)
    path2 = path_from_root(node2)
    lca = None

    for n1, n2 in zip(path1, path2):
        if n1 != n2:
            return lca
        lca = n1
    return lca

def lca_without_parent(root, node1, node2):
    if not root:
        print(f"no root: {root}")
        return None
    if root == node1 or root == node2:
        print(f"Either is root: {root.value}")
        return root
    if root:
        print(f"Root: {root.value}")

    if root.left:
        print(f"New left root: ", root.left.value)

    print(f"Before lca in left: Node1:{node1.value}, Node2:{node2.value} ")
    lca_in_left = lca_without_parent(root.left, node1, node2)

    if root.right:
        print(f"New right root: ", root.right.value)
    print(f"Before lca in right: Node1:{node1.value}, Node2:{node2.value} ")
    lca_in_right = lca_without_parent(root.right, node1, node2)


    if lca_in_left and lca_in_right:
        print(f"Lca in left: {lca_in_left.value}")
        print(f"Lca in right: {lca_in_right.value}")
        print(f"Root: {root.value}")
        return root
    else:
        if lca_in_left:
            print(f"Only Lca in left: {lca_in_left.value}")
        elif lca_in_right:
            print(f"Only Lca in right: {lca_in_right.value}")
    print("End ---- \n\n")
    return lca_in_left or lca_in_right


left6 =  BinaryNode(6, parent=None, left=None, right=None)
right4 =  BinaryNode(4, parent=None, left=None, right=None)
left4 =  BinaryNode(4, parent=None, left=None, right=None)
right2 =  BinaryNode(2, parent=None, left=None, right=None)

right3 =  BinaryNode(3, parent=None, left=left4, right=right2)
left9 =  BinaryNode(9, parent=None, left=None, right=None)

left5 =  BinaryNode(5, parent=None, left=left9, right=right3)
right8 =  BinaryNode(8, parent=None, left=left6, right=right4)

right20 =  BinaryNode(20, parent=None, left=None, right=None)

root = BinaryNode(10, parent=None, left=left5, right=right8)

print(lca_without_parent(root, left4, right20).value)