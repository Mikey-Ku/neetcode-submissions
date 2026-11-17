# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        leftHeight = self.maxheight(root.left)
        rightHeight = self.maxheight(root.right)
        
        d = leftHeight + rightHeight
        compare = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return max(compare, d)
    
    def maxheight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        return 1 + max(self.maxheight(root.left), self.maxheight(root.right))
