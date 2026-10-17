# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.counter = 0
        self.actualValue = 0
        self.inorderTraversal(root)

        return self.actualValue
    
    # Traverse the leftmost tree first.
    # This method allows us to visit smaller integers first, maintaining a counter
    # As this counter is maintained, once the counter == k, we know to return this specific value!
    def inorderTraversal(self, root: Optional[TreeNode]):
        if root is None:
            return
        
        self.inorderTraversal(root.left)

        self.counter += 1
        if self.counter == k:
            self.actualValue = root.val
        
        self.inorderTraversal(root.right)