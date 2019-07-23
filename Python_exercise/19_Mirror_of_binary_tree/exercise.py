class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    #change the exist tree
    def mirrorBinaryTree(self, root):
        if root == None:
            return None
        root.left, root.right = root.right, root.left
        self.mirrorBinaryTree(root.left)
        self.mirrorBinaryTree(root.right)
        return root
    
    #create the new tree
    def mirrorBinaryTree_2(self, root):
        if root == None:
            return None
        newTree = TreeNode(root.val)
        newTree.left = self.mirrorBinaryTree_2(root.left)
        newTree.right = self.mirrorBinaryTree_2(root.right)
        return newTree