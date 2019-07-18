class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def reContructBinaryTree(self, preorder, inorder):
        if not preorder and not inorder:
            return None
        root = TreeNode(preorder[0])
        if set(preorder) != set(inorder):
            return None
        i = inorder.index(preorder[0])
        root.left = self.reContructBinaryTree(preorder[1:i+1], inorder[:i])
        root.right = self.reContructBinaryTree(preorder[i+1:], inorder[i+1:])
        return root

    def backorder(self, root):
        if not root:
            return None
        while root:
            root = self.backorder(root.left, root.right)
            self.
            print(root.val)
preorder = [1, 2, 4, 7, 3, 5, 6, 8]
inorder = [4, 7, 2, 1, 5, 3, 8, 6]

solution = Solution()
newtree = solution.reContructBinaryTree(preorder, inorder)
print(newtree)