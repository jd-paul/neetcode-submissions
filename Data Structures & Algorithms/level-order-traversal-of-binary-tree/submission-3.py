# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        if new height is reached, append
        """
        if root is None:
            return []

        self.lst = []
        self.queue = []
        self.dfs(root, 0)

        return self.queue
    
    def dfs(self, root: Optional[TreeNode], currentHeight: int):
        if root is None:
            return
        
        if len(self.queue) <= currentHeight:
            self.queue.append([])
        
        lst = self.queue
        lst[currentHeight].append(root.val)

        if not root.left is None:
            self.dfs(root.left, currentHeight+1)
        if not root.right is None:
            self.dfs(root.right, currentHeight+1)