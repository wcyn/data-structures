class Tree:
    """Abstract base class representing a tree structure."""

    # Nested Position class
    class Position:
        """
        An abstraction representing the location of a single element.
        """

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError("must be implemented by subclass")

        def eq (self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError("must be implemented by subclass")

        def ne (self, other):
            """Return True if other does not represent the same location."""
            return not (self == other) # opposite of eq

    # Abstract methods that concrete subclass must support=
    def root(self):
        """
        Return Position representing the tree s root (or None if empty).
        """
        raise NotImplementedError("must be implemented by subclass")

    def parent(self, p):
        """
        Return Position representing p s parent (or None if p is root).
        """
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        """
        Return the number of children that Position p has.
        """
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        """
        Generate an iteration of Positions representing p s children.
        """
        raise NotImplementedError("must be implemented by subclass")

    def len (self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError("must be implemented by subclass")

    def is_root(self, p):
        """O(1)"""
        return self.root() == p

    def is_leaf(self, p):
        """O(1)"""
        return self.num_children(p) == 0

    def is_empty(self):
        """O(1)"""
        return len(self) == 0

    def depth(self, p):
        """O(dp+1)
        O(n) worst case if all nodes form a single branch"""
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))

    def _height1(self):
        """Return the height of the tree O(n^2)"""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        """ Return the height of the subtree rooted at Position p O(n)"""
        # print("Getting height")
        if self.is_leaf(p):
            return 0
        return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """O(n)
        Return height of the sub-tree rooted at Position p
        If p is None, return the height of the entire tree
        """
        if p is None:
            p = self.root()
        return self._height2(p)

class BinaryTree(Tree):
    """
    Abstract base class representing a binary tree structure
    """

    # Additional Abstract methods
    def left(self, p):
        """
        Return a position representing p's left child. Return None if
        p does not have a left child
        """
        raise NotImplementedError("Must be implemented by subclass")

    def right(self, p):
        """
        Return a position representing p's right child. Return None if
        p does not have a right child
        """
        raise NotImplementedError("Must be implemented by subclass")

    # Concrete methods
    def sibling(self, p):
        """O(1)
        Return a position representing p's sibling (or None if no sibling)
        """
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """O(1)
        Generate an iteration of Positions representing p's children
        """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

class LinkedBinaryTree(BinaryTree):
    """
    Linked Representations of a binary tree structure
    """

    class _Node: # lightweight, non-public class for storing a node
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """
        An abstraction representing the location of a single element
        """

        def __init__(self, container, node):
            """ Constructor should not be invoked by user"""
            self._container = container
            self._node = node

        def element(self):
            """
            Return the lelement stored at this postition
            """
            return self._node._element

        def __eq__(self, other):
            """
            Return True if other is a position representing the same location
            """
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """
        Return associated node, if position is valid
        """
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position type')
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node: # convention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """
        Return Position instance for given node (or None if no node)
        """
        return self.Position(self, node) if node is not None else None

    # Binary tree constructor
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root = None
        self._size = 0

    # Public accessors
    def len (self):
        """ O(1)
        Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """O(1)
        Return the root Position of the tree (or None if tree is empty).
        """
        return self._make_position(self._root)

    def parent(self, p):
        """O(1)
        Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """O(1)
        Return the Position of p's left child (or None if no left child).
        """
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """O(1)
        Return the Position of p's right child (or None if no right child).
        """
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """O(1)
        Return the number of children of Position p.
        """
        node = self._validate(p)
        count = 0
        if node._left is not None: # left child exists
            count += 1
        if node._right is not None: # right child exists
            count += 1
        return count

    def add_root(self, e):
        """O(1)
        Place element e at the root of an empty tree and return new Position.
        Raise ValueError if tree nonempty.
        """
        if self._root is not None:
            raise ValueError("Root exists")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def add_left(self, p, e):
        """O(1)
        Create a new left child for Position p, storing element e.
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child.
        """
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Left child exists")
        self._size += 1
        node._left = self._Node(e, node) # node is its parent
        return self._make_position(node._left)

    def add_right(self, p, e):
        """O(1)
        Create a new right child for Position p, storing element e.
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child exists")
        self._size += 1
        node._right = self._Node(e, node) # node is its parent
        return self._make_position(node._right)

    def replace(self, p, e):
        """O(1)
        Replace the element at position p with e, and return old element.
        """
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def delete(self, p):
        """O(1)
        Delete the node at Position p, and replace it with its child, if any.
        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError("p has two children")
        child = node._left if node._left else node._right # might be None
        if child is not None:
            child._parent = node._parent # child's grandparent becomes parent
        if node is self._root:
            self._root = child # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node # convention for deprecated node
        return node._element

    def attach(self, p, t1, t2):
        """O(1)
        Attach trees t1 and t2 as left and right subtrees of external p.
        """
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError("position must be leaf")
        if not type(self) is type(t1) is type(t2): # all trees must be same type
            raise TypeError("Tree types must match")
        self._size += len(t1) + len(t2)
        if not t1.is_empty( ): # attached tas left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty(): # attached tas right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None # set t2 instance to empty
            t2._size = 0

linked_binary_tree = LinkedBinaryTree()
root = linked_binary_tree.add_root(4)
print("The value of root: ", linked_binary_tree.root().element()) # Output: 4

print("Root we added is actual root? ", root == linked_binary_tree.root()) # Output: True

left_child = linked_binary_tree.add_left(root, 1)
print("First child: ", next(linked_binary_tree.children(root)).element()) # Output: 1

right_child = linked_binary_tree.add_right(root, 5)
children = linked_binary_tree.children(root)

print("First child: ", next(children).element()) # Output: 1
print("Second child: ", next(children).element()) # Output: 5

lbt = linked_binary_tree
print("Root children: ", lbt.num_children(root)) # Output 2
print("Root grandchildren: ", lbt.num_children(lbt.left(root))) # Output 0
print("Length of tree: ", lbt.len())

l_left_child = lbt.add_left(left_child, -1)
r_left_child = lbt.add_right(left_child, 2)

parent_of_left = lbt.parent(left_child)
print("Parent of left child is root? ", lbt.is_root(parent_of_left)) # True

print("Depth at root: ", lbt.depth(root)) # 0
print("Depth at left child of left child: ", lbt.depth(l_left_child)) # 2

print("Height at root: ", lbt.height()) # 2
print("Height at left child: ", lbt.height(left_child)) # 1
print("Height at right child of left child: ", lbt.height(r_left_child)) # 0

# Replace
# initially -1
print("Replaced left child of left child: ", lbt.replace(l_left_child, -4)) # 1
print("New left child of left child: ", l_left_child.element())