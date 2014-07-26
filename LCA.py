
class TreeNode:
    def __init__(self, k):
        self.k = k
        self.left = None
        self.right = None

    def isLeaf(self):
        return self.left is None and self.right is None

    def hasLeft(self):
        return self.left is not None

    def hasRight(self):
        return self.right is not None

    def hasLeftOnly(self):
        return self.left is not None and self.right is None

    def hasRightOnly(self):
        return self.left is None and self.right is not None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def LCA(self, k1, k2):
        if self.get(k1) is None or self.get(k2) is None: return None
        return self._LCA(self.root, k1, k2)

    def _LCA(self, current, k1, k2):
        if current is None: return None
        if current.k == k1 or current.k == k2: return current
        l = self._LCA(current.left, k1, k2)
        r = self._LCA(current.right, k1, k2)
        if l and r: return current
        if l is not None: return l
        else: return r

    def get(self, k):
        return self._get(self.root, k)

    def _get(self, current, k):
        if current is None: return None
        if current.k == k: return current
        r = self._get(current.left, k)
        if r is not None: return r
        return self._get(current.right, k)

    def put(self, k):
        if self.root is None:
            self.root = TreeNode(k)
        else:
            self._put(self.root, k)

    def _put(self, current, k):
        if k < current.k:
            if current.hasLeft():
                self._put(current.left, k)
            else:
                self.left = TreeNode(k)
        else:
            if current.hasRight():
                self._put(current.right, k)
            else:
                self.right = TreeNode(k)


if __name__ == '__main__':
    BinaryTree()
