# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode()
        dummy.right = root

        current = root
        if current is None:
            return None
        elif current.left is None and current.right:
            current.left = current.right
            current.right = None
            self.invertTree(current.left)
        elif current.right is None and current.left:
            current.right = current.left
            current.left = None
            self.invertTree(current.right)
        elif current.left and current.right:
            left = current.left
            right = current.right

            current.left = right
            current.right = left
            self.invertTree(current.left)
            self.invertTree(current.right)

        return dummy.right
