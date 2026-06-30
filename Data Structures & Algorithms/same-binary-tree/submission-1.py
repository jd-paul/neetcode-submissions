class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        current_a = p
        current_b = q

        # Hard check statements
        if not current_a and not current_b:
            return True
        if not current_a or not current_b or current_a.val != current_b.val:
            return False
        
        current_a_left = current_a.left
        current_a_right = current_a.right

        current_b_left = current_b.left
        current_b_right = current_b.right

        # Move onto the next node

        return self.isSameTree(current_a_left, current_b_left) and self.isSameTree(current_a_right, current_b_right)