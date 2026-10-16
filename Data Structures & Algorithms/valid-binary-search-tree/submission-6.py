# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))

    def helper(self, node: Optional[TreeNode], low: int, high: int):
        if node is None:
            return True

        if not (low < node.val < high):
            return False
        
        return self.helper(node.left, low, node.val) and self.helper(node.right, node.val, high)
    