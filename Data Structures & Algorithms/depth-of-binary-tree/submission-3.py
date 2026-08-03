# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        current = root

        if not current:
            return 0
        else:
            l = current.left
            r = current.right

            return 1 + max(self.maxDepth(l), self.maxDepth(r))