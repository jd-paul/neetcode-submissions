# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lst = []

        current = head
        while current:
            lst.append(current)
            current = current.next


        dummy = ListNode()
        dummy.next = head
        current = None
        
        # [0, n-1, 1, n-2, 2, n-3, ...] is the logic
        # Odd becomes 0, 1, 2, 3. Counter-th node
        # Even becomes n-counter-th node

        left, right = 0, len(lst) - 1
        
        while left < right:
            # Point left to right
            lst[left].next = lst[right]
            left += 1
            
            # If we met in the middle, break to avoid self-loop
            if left == right:
                break
                
            # Point right to the next left
            lst[right].next = lst[left]
            right -= 1
            
        # 3. CRITICAL: Break the cycle
        # The node at the 'left' index is now the new tail.
        # It must point to None.
        lst[left].next = None