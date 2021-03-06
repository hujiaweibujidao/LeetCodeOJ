# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if root == None: return []
        res = []
        self.preorder_rec(root, res)
        return res

    def preorder_rec(self, root, res):
        if root == None: return
        res.append(root.val)
        if root.left:
            self.preorder_rec(root.left, res)
        if root.right:
            self.preorder_rec(root.right, res)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left=None
    node = TreeNode(2)
    root.right=node
    node.left = TreeNode(3)
    node.right=None
    print Solution().postorderTraversal(root)
    root = None
    print Solution().postorderTraversal(root) #[]

