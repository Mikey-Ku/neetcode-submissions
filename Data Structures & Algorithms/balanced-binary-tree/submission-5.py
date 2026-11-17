# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            
            left_v = height(node.left)
            right_v = height(node.right)

            if left_v == -1 or right_v == -1:
                return -1
            
            if abs(left_v - right_v) > 1:
                return -1
            
            return 1 + max(left_v, right_v)
        
        return height(root) != -1


