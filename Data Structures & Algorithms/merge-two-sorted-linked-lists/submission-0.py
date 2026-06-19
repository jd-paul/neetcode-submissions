# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_ptr = ListNode(0)
        prev = dummy_ptr
                
        pointer_a = list1
        pointer_b = list2

        while pointer_a or pointer_b:
            if pointer_a and pointer_b:
                if pointer_a.val <= pointer_b.val:
                    prev.next = pointer_a
                    prev = prev.next
                    pointer_a = pointer_a.next
                    
                else:
                    prev.next = pointer_b
                    prev = prev.next
                    pointer_b = pointer_b.next
            
            elif pointer_a and not pointer_b:
                prev.next = pointer_a
                prev = prev.next
                pointer_a = pointer_a.next

            elif pointer_b and not pointer_a:
                prev.next = pointer_b
                prev = prev.next
                pointer_b = pointer_b.next
            
            else:
                break

        return dummy_ptr.next
