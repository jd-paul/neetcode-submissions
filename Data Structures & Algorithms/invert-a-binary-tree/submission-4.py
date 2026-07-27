# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode()
        dummy.left = root

        def dfs(current: Optional[TreeNode]):
            if current is None:
                return
            left = current.left
            right = current.right

            current.left = right
            current.right = left

            dfs(current.left)
            dfs(current.right)

        dfs(root)
        return dummy.left