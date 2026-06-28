# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:                                                            
        dummy = ListNode()                                                                                                                         
        dummy.next = head                                                                                                                          
                                                                                                                                                
        list_size = 0                                                                                                                              
        current = head                                                                                                                             
        while current:                                                                                                                             
            list_size += 1                                                                                                                         
            current = current.next                                                                                                                 
                                                                                                                                                
        node = list_size - n                                                                                                                       
                                                                                                                                                
        if node == 0:                                                                                                                              
            return dummy.next.next                                                                                                                 
                                                                                                                                                
        counter = 0                                                                                                                                
        current = head                                                                                                                             
        prev = head                                                                                                                                
                                                                                                                                                
        while current:                                                                                                            
            if counter == node:                                                                                                                    
                prev.next = current.next                                                                                                           
                break                                                                                                                              
            else:                                                                                                                                  
                counter += 1                                                                                                                       
                prev = current                                                                                                                     
                current = current.next                                                                                                             
                                                                                                                                                
        return dummy.next