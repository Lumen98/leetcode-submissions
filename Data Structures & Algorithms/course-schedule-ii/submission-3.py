from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        self.graph = {}
        self.res = []

        for i in range(numCourses):
            self.graph[i] = []
        
        for crs, pre in prerequisites:
            self.graph[crs].append(pre)

        white = set(self.graph.keys())
        grey = set()
        black = set()

        while white:
            curr = white.pop()

            if not self.dfs(curr, grey, black):
                return []
        
        return self.res

    def dfs(self, crs, grey, black):
        grey.add(crs)

        for pre in self.graph[crs]:
            if pre in grey:
                return False
            if not self.dfs(pre, grey, black):
                return False
            
            
        

        grey.remove(crs)
        if crs not in black:
            self.res.append(crs)
        black.add(crs)
        
        return True
                









