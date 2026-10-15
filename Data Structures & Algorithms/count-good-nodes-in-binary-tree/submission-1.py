# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.nodeCount = 0
        self.dfs(root, root.val)

        return self.nodeCount
    
    def dfs(self, node: TreeNode, localMax: int) -> list:
        if node is None:
            return
        
        if node.val >= localMax:
            self.nodeCount += 1
        localMax = max(node.val, localMax)

        if node.left:
            self.dfs(node.left, localMax)
        
        if node.right:
            self.dfs(node.right, localMax)