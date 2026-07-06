"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        prev = dummy
        current = head

        # Create a dictionary storing the copy of the original node's `.random`.
        dct = {}

        def finderFunction(value):
            current = prev.next
            while current:
                if current.val == val:
                    return current
                
                current = current.next
            return None

        # Iterate through and connect them to the next.
        while current:
            new_node = Node(current.val)
            prev.next = new_node
            
            # Map original to copy.
            dct[current] = new_node
            
            prev = new_node
            current = current.next

        # Second pass where we now properly wire up the random values.
        # key, value = copy, original
        for original_node, copy_node in dct.items():            
            if original_node.random is None:
                copy_node.random = None
            else:
                
                copy_node.random = dct[original_node.random]

        
        return dummy.next