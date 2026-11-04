class Solution:
    """
    Sample input: [
        [0, 1], [0, 2],
        [1, 3], [1, 4],
        [3, 4]
    ]
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.preMap = {}
        self.outerVisited = {}

        for lst in prerequisites:
            crs, pre = lst[0], lst[1]
            if crs not in self.preMap:
                self.preMap[crs] = [pre]
            else:
                self.preMap[crs].append(pre)

            if pre not in self.preMap:
                self.preMap[pre] = []
        
        for key, value in self.preMap.items():
            if not self.dfs(key, value, {}):
                return False
            
        return True

    def dfs(self, crs: int, pre: list, visited: dict) -> bool[Optional]:
        if visited is None:
            return
        if crs in visited:
            return False
        if crs in self.outerVisited:
            return self.outerVisited[crs]
        
        self.outerVisited[crs] = True
        visited[crs] = 1
        visited_copy = visited.copy()
        for node in pre:
            if not self.dfs(node, self.preMap[node], visited_copy):
                self.outerVisited[crs] = False
                return False
        return True