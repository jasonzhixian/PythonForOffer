#6
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #reconstructbinarytree
    def reConstructBinaryTree(self, preorder, inorder):
        if not preorder and not inorder:
            return None
        root = TreeNode(preorder[0])
        if set(preorder) != set(inorder):
            return None
        i = preorder.indes(inorder[0])
        root.left = self.reConstructBinaryTree(preorder[1, i+1], inorder[:i])
        root.right = self.reConstructBinaryTree(preorder[i+1], inorder[i+1:])
        return root

    def preorder(self, root):
        if root is None:
            return None
        print(root.val, end = '')
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        if root is None:
            return None
        self.inorder(root.left)
        print(root.val, end = '')
        self.inorder(root.right)
    
    def backorder(self, root):
        if root is None:
            return None
        self.backorder(root.left)
        self.backorder(root.right)
        print(root.val, end = '')

#39
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #maximum depth of binary tree
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    
    #minimum depth of binary tree
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
    
    
#19
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #change the exist tree
    def mirrorBinaryTree(self, root):
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.mirrorBinaryTree(root.left)
        self.mirrorBinaryTree(root.right)        
        return root
    
    #create the new tree
    def mirrorBinaryTree(self, root):
        if root is None:
            return None
        newtree = TreeNode(root.val)
        newtree.left = self.mirrorBinaryTree(root.left)
        newtree.right = self.mirrorBinaryTree(root.right)
        return newtree

#pathSum
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        if root.left is None and root.right is None and root.val == sum:
            return True
        else:
            return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-roo.val)

#is symmetric_tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        self.isSymmetricRe(root.left, root.right)

    def isSymmetricRe(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.isSymmetricRe(left.left, right.right) and self.isSymmetricRe(left.right, right.left)


#binary tree level order traversal / reverse
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root): #def levelOrderBottom
        if root is None:
            return []
        result, cur = [], [root]
        while cur:
            next_level, vals = [], []
            for node in cur:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur = next_level
            result.append(vals)
        return result #return result[::-1]

        
            
   #39_2 is balanced binary tree
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #solution one
    def getDepth(self, root):
        if root is None:
            return 0
        else:
            return max(self.getDepth(root.left), self.getDepth(root.right)) + 1

    def isBalanced(self):
        if root is None:
            return True
        if abs(self.getDepth(root.left) - self.getDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

