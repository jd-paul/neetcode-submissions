class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.numCourses = numCourses
        self.traversed = {}
        self.result = []
        self.completed = {}

        self.preMap = {course: [] for course in range(numCourses)}

        for lst in prerequisites: # preMap
            a, b = lst[0], lst[1]

            if a not in self.preMap:
                self.preMap[a] = [b]
            else:
                self.preMap[a].append(b)

            if b not in self.preMap:
                self.preMap[b] = []
        
        for a in range(0, numCourses):
            if not self.dfs(a, self.traversed):
                return []
        
        return self.result
    
    def dfs(self, node: int, traversed: dict):
        if node in traversed and traversed[node] == 1: # Failure cases
            return False
        if node in self.completed:
            return True
        
        lst = self.preMap[node]
        traversed[node] = 1
        for n in lst:
            traversed_copy = traversed.copy()
            if not self.dfs(n, traversed_copy):
                return False
            self.completed[node] = 1
        
        traversed[node] = 0
        self.completed[node] = 1
        self.result.append(node)
        return True