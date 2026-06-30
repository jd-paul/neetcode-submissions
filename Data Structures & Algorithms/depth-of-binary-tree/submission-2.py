# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        current = root
        if current:
            if current.left and current.right:
                return 1 + max(self.maxDepth(current.left), self.maxDepth(current.right))
            elif current.left and not current.right:
                return 1 + self.maxDepth(current.left)
            elif current.right and not current.left:
                return 1 + self.maxDepth(current.right)
            else:
                return 1
        else:
            return 0