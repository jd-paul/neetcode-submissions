# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        
        def height(root):
            if root is None:
                return 0
            
            d_l = height(root.left)
            d_r = height(root.right)

            self.d = max(self.d, d_l + d_r)
            return 1 + max(d_l, d_r)
        
        height(root)
        return self.d