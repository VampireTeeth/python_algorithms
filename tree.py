class NotImplementedError(Exception):
  """
  An error indicating not implemented
  """
  def __init__(self, err):
    Exception.__init__(self, err)


class Tree:
  """
  An abstraction representing a tree
  """

  class Position:
    """
    An abstraction representing the location of a single element
    """

    def element(self):
      raise NotImplementedError('must be implemented by subclass')

    def __eq__(self, other):
      raise NotImplementedError('must be implemented by subclass')

    def __ne__(self, other):
      raise NotImplementedError('must be implemented by subclass')

  def root(self):
    """
    Return position of the root node
    """
    raise NotImplementedError('must be implemented by subclass')

  def parent(self, p):
    """
    Return the parent of the position p
    """
    raise NotImplementedError('must be implemented by subclass')

  def num_children(self, p):
    """
    Return the number of children position p has
    """
    raise NotImplementedError('must be implemented by subclass')

  def children(self, p):
    """
    Return an iteration of Positions representing p's children
    """
    raise NotImplementedError('must be implemented by subclass')

  def __len__(self):
    """
    Return the total number of elements in the tree
    """
    raise NotImplementedError('must be implemented by subclass')

  def is_root(self, p):
    """
    Return True if Position p is root of the tree
    """
    return self.root() == p

  def is_leaf(self, p):
    """
    Return True if Position p is a leaf
    """
    return self.num_children(p) == 0

  def is_empty(self):
    """
    Return True if the tree is empty
    """
    return len(self) == 0



class BinaryTree(Tree):
  """
  An abstraction of binary tree data structure
  """
  def left(self, p):
    """
    Return a Position that represents the left child of Position p
    """
    raise NotImplementedError('must be implemented by subclass')

  def right(self, p):
    """
    Return a Position that represents the right child of Position p
    """
    raise NotImplementedError('must be implemented by subclass')


  def sibling(self, p):
    """
    Return a Position that represents the sibling of Position p
    or None if no sibling found
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
    if self.left(p) is not None:
      yield self.left(p)
    if self.right(p) is not None:
      yield self.right(p)
