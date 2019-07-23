#leetcode 101 Symmetric Tree
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.isSymmetricRe(root.left, root.right)

    def isSymmetricRe(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isSymmetricRe(left.left, right.right) and self.isSymmetricRe(left.right, right.left) 