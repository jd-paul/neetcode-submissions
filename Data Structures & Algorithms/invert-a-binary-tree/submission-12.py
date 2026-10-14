# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head = root

        if root is None:
            return None
        
        self.recursiveFunction(root)
        return head
        
    
    def recursiveFunction(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root.left and not root.right:
            return None
        
        elif root.left and not root.right:
            l = root.left
            r = None
            root.right = l
            root.left = r

            return self.recursiveFunction(l)

        elif root.right and not root.left:
            l = None
            r = root.right
            root.left = r
            root.right = l

            return self.recursiveFunction(r)

        elif root.left and root.right:
            l = root.left
            r = root.right
            
            root.left = r
            root.right = l
            return self.recursiveFunction(l), self.recursiveFunction(r)