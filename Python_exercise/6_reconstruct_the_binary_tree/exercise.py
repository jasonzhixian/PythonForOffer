#!/usr/bin/env python 
'''the following script is the reconstruction of tree based on the preorder\
and inorder and three ways of travel of the tree'''

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

    def pre_order(self, root):
        if root is None:
            return None
        print(root.val, end = "")
        self.pre_order(root.left)
        self.pre_order(root.right)

    def in_order(self, root):
        if root is None:
            return None
        self.in_order(root.left)
        print(root.val, end = "")
        self.in_order(root.right)

    def back_order(self, root):
        if root is None:
            return None
        self.back_order(root.left)
        self.back_order(root.right)
        print(root.val, end = "")
        
preorder = [1, 2, 4, 7, 3, 5, 6, 8]
inorder = [4, 7, 2, 1, 5, 3, 8, 6]

solution = Solution()
newtree = solution.reContructBinaryTree(preorder, inorder)
print(newtree)
solution.pre_order(newtree)
print('')
solution.in_order(newtree)
print('')
solution.back_order(newtree)
print('')