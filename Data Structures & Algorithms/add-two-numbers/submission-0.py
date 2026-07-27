# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1 = l1
        curr_2 = l2

        num_1 = ""
        while curr_1:
            num_1 += f"{curr_1.val}"
            curr_1 = curr_1.next
        num_1 = num_1[::-1]
        num_1 = int(num_1)        

        num_2 = ""
        while curr_2:
            num_2 += f"{curr_2.val}"
            curr_2 = curr_2.next
        num_2 = num_2[::-1]
        num_2 = int(num_2)

        final_num = num_1 + num_2
        final_string = str(final_num)[::-1]

        dummy_node = ListNode()
        curr = dummy_node

        for i in final_string:
            curr.next = ListNode(int(i))
            curr = curr.next

        return dummy_node.next