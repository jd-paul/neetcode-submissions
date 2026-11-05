class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.outer_visited = {}
        self.preMap = {}
        
        # First pass
        for requisite in prerequisites:
            crs, pre = requisite[0], requisite[1]

            if crs not in self.preMap:
                self.preMap[crs] = [pre]
            else:
                self.preMap[crs].append(pre)
            if pre not in self.preMap:
                self.preMap[pre] = []


        # Second pass
        for i in range(0, numCourses):
            if i not in self.preMap:
                continue
            if not self.dfs(i, []):
                return False
        
        return True

    def dfs(self, crs, visited: list) -> bool:
        if not self.preMap[crs]:
            return True
        
        
        if crs in visited:
            return False
        if crs in self.outer_visited:
            return True
        
        visited.append(crs)
        self.outer_visited[crs] = 1
        
        # DFS on the remaining values

        for new_node in self.preMap[crs]:
            visited_copy = visited.copy()            
            if not self.dfs(new_node, visited_copy):
                return False

        visited.remove(crs)
        return True


