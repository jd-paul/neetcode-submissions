# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        current = root
        isBalanced = True

        def balanceChecker(new_current: Optional[TreeNode]):
            nonlocal isBalanced
            if new_current:
                if new_current.left and new_current.right:
                    leftHeight = balanceChecker(new_current.left)
                    rightHeight = balanceChecker(new_current.right)

                    if abs(leftHeight - rightHeight) > 1:
                        isBalanced = False
                    
                    return max(leftHeight, rightHeight) + 1
                elif new_current.left and not new_current.right:
                    leftHeight = balanceChecker(new_current.left)
                    rightHeight = balanceChecker(new_current.right)
                    if abs(leftHeight - rightHeight) > 1:
                        isBalanced = False
                    return max(leftHeight, rightHeight) + 1

                elif new_current.right and not new_current.left:
                    leftHeight = balanceChecker(new_current.left)
                    rightHeight = balanceChecker(new_current.right)
                    if abs(leftHeight - rightHeight) > 1:
                        isBalanced = False

                    return max(leftHeight, rightHeight) + 1
                else:
                    return 1
            else:
                return 0
        
        balanceChecker(current)

        return isBalanced