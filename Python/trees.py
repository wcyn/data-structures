class Tree:
    """Abstract base class representing a tree structure."""

    # Nested Position class
    class Position:
    """An abstraction representing the location of a single element."""

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
    """Return Position representing the tree s root (or None if empty)."""
    raise NotImplementedError( must be implemented by subclass )

    def parent(self, p):
    """Return Position representing p s parent (or None if p is root)."""
    raise NotImplementedError("must be implemented by subclass")

    def num children(self, p):
    """Return the number of children that Position p has."""
    raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
    """Generate an iteration of Positions representing p s children."""
    raise NotImplementedError("must be implemented by subclass")

    def len (self):
    """Return the total number of elements in the tree."""
    raise NotImplementedError("must be implemented by subclass")

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        """O(n) worst case if all nodes form a single branch"""
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))

    def _height1(self):
        """Return the height of the tree O(n^2)"""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        """ Return the height of the subtree rooted at Position p O(n)"""
        if self.is_leaf(p):
            return 0
        return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """
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
        """
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
        """
        Generate an iteration of Positions representing p's children
        """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
