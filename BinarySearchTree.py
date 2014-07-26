class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, k, v):
        self.put(k, v)


    def __getitem__(self, k):
        return self.get(k)

    def __contains__(self, k):
        if self._get(self.root, k): return True
        else: return False

    def put(self, key, val):
        if self.root is None:
            self.root = TreeNode(key, val)
        else:
            self._put(self.root, key, val)

    def _put(self, treeNode, key, val):
        if key == treeNode.key:
            treeNode.val = val
        elif key < treeNode.key:
            if treeNode.hasLeft():
                self._put(treeNode.left, key, val)
            else:
                treeNode.left = TreeNode(key, val)
                self.size += 1
        else:
            if treeNode.hasRight():
                self._put(treeNode.right, key, val)
            else:
                treeNode.right = TreeNode(key, val)
                self.size += 1

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, treeNode, key):
        if treeNode is None: return None
        if treeNode.key == key: return treeNode.val

        if key < treeNode.key:
            return self._get(treeNode.left, key)
        else:
            return self._get(treeNode.right, key)

    def delete(self, key):
        if self.size > 1:
            if self._get(self.root, key):
                self.remove(None, self.root, key)
            else:
                raise KeyError("Key not in tree")
        elif self.size == 1:
            if self.key == key:
                self.root = None
                self.size -= 1
            else:
                raise KeyError("Key not in tree")
        else:
            raise KeyError("Key not in tree")
                
    def remove(self, parent, current, key):
        if current.key == key:
            self._remove(parent, current, key)
        elif key < current.key:
            self.remove(current, current.left, key)
        else:
            self.remove(current, current.right, key)

    def _remove(self, parent, current, key):
        if current.isLeaf():
            if parent is None:
                self.root = None
                self.size = 0
            else:
                self._removeLeafChild(parent, key)
                self.size -= 1
        elif current.hasLeft() and not current.hasRight():
            if parent.left.key == current.key:
                parent.left = current.left
            else:
                parent.right = current.left
            current.left = None
            self.size -= 1
        elif current.hasRight() and not current.hasLeft():
            if parent.left.key == current.key:
                parent.left = current.right
            else:
                parent.right = current.right
            current.right = None
            self.size -= 1
        else:
            leftMost = self._leftMost(current.right)
            leftMost.left = current.left

            if parent.left.key == current.key:
                parent.left = current.right
            elif parent.right.key == current.key:
                parent.right = current.right

            current.left = None
            current.right = None
            self.size -= 1

    def _removeLeafChild(self, parent, key):
        if parent is None: return

        if parent.hasLeft() and parent.left.key == key:
            parent.left = None
        elif parent.hasRight() and parent.right.key == key:
            parent.right = None

    def _leftMost(self, current):
        if current.isLeaf() or not current.hasLeft(): return current
        return self._leftMost(current.left)

    def _ancestors(self, current, key):
        if current is None: return None
        else:
            if key == current.key:
                return []
            elif key < current.key:
                r = self._ancestors(current.left, key) 
                
            else:
                r = self._ancestors(current.right, key)

            if r is not None: return [current] + r
            else: return None

    def printTree(self):
        print "-" * 20
        self._printTree(self.root)

    def _printTree(self, current):
        if current.hasLeft(): self._printTree(current.left) 
        print "%s = %s : %s" % (current.key, current.val, [n.key for n in self._ancestors(self.root, current.key)])
        if current.hasRight(): self._printTree(current.right)

        

class TreeNode:
    def __init__(self, key, val, left= None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

    def hasLeft(self):
        return self.left is not None

    def hasRight(self):
        return self.right is not None

    def isLeaf(self):
        return self.left is None and self.right is None

    def left(self):
        return self.left

    def right(self):
        return self.right


if __name__ == '__main__':
    lst = [7,2,4,1,6,8,11,15,10,3]
    bst = BinarySearchTree()
    for i in lst:
        bst.put(i,i)
    bst.put(9,9)
    bst.printTree()
    print bst.get(7)
    print bst[7]
    bst.delete(8)
    bst.printTree()
    bst.delete(2)
    bst.printTree()
    bst.put(13, 13)
    bst.put(14, 14)
    bst.printTree()
    bst.delete(13)
    bst.printTree()

    bst[3] = "three"
    bst.printTree()


