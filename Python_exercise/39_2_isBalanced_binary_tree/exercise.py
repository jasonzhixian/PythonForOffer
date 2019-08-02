class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#solution one
class Solution(object):
    def getDepth(self, root):
        if root == None:
            return 0
        else:
            return max(self.getDepth(root.left), self.getDepth(root.right)) + 1

    def isBalanced(self, root):
        if root == None:
            return True
        if abs(self.getDepth(root.left) - self.getDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

#solution two
class Solution(object):
    def isBalanced(self, root):
        def getHeight(root):
            if root is None:
                return 0 
            left_height, right_height = getHeight(root.left), getHeight(root.right)
            if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        return (getHeight(root) >= 0)