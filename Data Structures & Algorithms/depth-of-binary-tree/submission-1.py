# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        current = root
        if current and current.left and current.right:
            return 1 + max(self.maxDepth(current.left), self.maxDepth(current.right))
        elif current and not current.right and current.left:
            return 1 + max(self.maxDepth(current.left), 0)
        elif current and not current.left and current.right:
            return 1 + max(self.maxDepth(current.right), 0)
        elif current and not current.left and not current.right:
            return 1
        else:
            return 0