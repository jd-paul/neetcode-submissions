# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowPtr = head
        fastPtr = head

        while slowPtr and fastPtr and fastPtr.next and fastPtr.next.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

            if slowPtr == fastPtr:
                return True
        
        return False