# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        self.queue = []
        self.output = []
        self.bfs(root, 0)

        for lst in self.queue:
            self.output.append(lst[-1])

        return self.output
    
    def bfs(self, root: Optional[TreeNode], currentHeight: int):
        cur = root

        if cur is None:
            return

        if len(self.queue) <= currentHeight:
            self.queue.append([])
        
        queue = self.queue
        queue[currentHeight].append(root.val)

        if not root.left is None:
            self.bfs(root.left, currentHeight+1)
        if not root.right is None:
            self.bfs(root.right, currentHeight+1)