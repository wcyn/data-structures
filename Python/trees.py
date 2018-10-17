class Tree:
    """Abstract base class representing a tree structure."""

    #------------------------------- nested Position class -------------------------------
    class Position:
    """An abstraction representing the location of a single element."""

        def element(self):
        """Return the element stored at this Position."""
        raise NotImplementedError( must be implemented by subclass )

        def eq (self, other):
        """Return True if other Position represents the same location."""
        raise NotImplementedError( must be implemented by subclass )

        def ne (self, other):
        """Return True if other does not represent the same location."""
        return not (self == other) # opposite of eq

    # ---------- abstract methods that concrete subclass must support ----------
    def root(self):
    """Return Position representing the tree s root (or None if empty)."""
    raise NotImplementedError( must be implemented by subclass )

    def parent(self, p):
    """Return Position representing p s parent (or None if p is root)."""
    raise NotImplementedError( must be implemented by subclass )

    def num children(self, p):
    """Return the number of children that Position p has."""
    raise NotImplementedError( must be implemented by subclass )

    def children(self, p):
    """Generate an iteration of Positions representing p s children."""
    raise NotImplementedError( must be implemented by subclass )

    def len (self):
    """Return the total number of elements in the tree."""
    raise NotImplementedError( must be implemented by subclass )

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0