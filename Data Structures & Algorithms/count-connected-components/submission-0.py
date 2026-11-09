class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        For each node, keep finding its parent and simplifying accordingly.

        From par = [0, 1, 2, 3, 4]
        We will end up with par = [0, 0, 0, 3, 3]
        We unionise. Here, we unionised three times.

        5 - 3 = 2. Therefore there are 2 disjoint graphs.
        """

        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1): # Find its root parent
            res = n1

            while res != par[res]:
                par[res] = par[par[res]] # A way to simplify so we reach its grandparent
                res = par[res] # Go up that chain until we reach parent
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
        
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res