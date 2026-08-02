# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode()
        current = root
        dummy.left = root
        

        def dfs(current):
            if current is None:
                return

            l = current.left
            r = current.right

            current.left = r
            current.right = l

            dfs(current.left)
            dfs(current.right)
        
        dfs(current)

        return dummy.left