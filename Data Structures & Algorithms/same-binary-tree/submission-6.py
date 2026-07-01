# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        isSameTree = True

        # Outer value pattern where we keep looking for proof that it's wrong
        def checkTree(p: Optional[TreeNode], q: Optional[TreeNode]):
            nonlocal isSameTree
            if not p and not q:
                return True
            if not p or not q or q.val != p.val:
                isSameTree = False
                return False

            p_left, p_right = p.left, p.right
            q_left, q_right = q.left, q.right

            return checkTree(p_left, q_left) and checkTree(p_right, q_right)
        
        return checkTree(p, q)
        # return isSameTree