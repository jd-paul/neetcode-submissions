"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Two pass aproach
        """
        self.dct = {}
        return self.recurse(node)

    def recurse(self, node: Optional['Node']):
        if node is None:
            return None
        if node.val in self.dct:
            return self.dct[node.val]
        
        copy = Node(node.val, None)

        self.dct[copy.val] = copy
        
        if node.neighbors is None:
            return
        
        for n in node.neighbors:
            copy.neighbors.append(self.recurse(n))
        
        return copy