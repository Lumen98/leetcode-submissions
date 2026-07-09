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

        



    def dfs(self, curr, grey, black):
        if curr in grey:
            return False

        grey.add(curr)

        for nei in self.graph[curr]:
            if not self.dfs(nei, grey, black):
                return False
        
        grey.remove(curr)
        if curr not in black:
            self.res.append(curr)
        black.add(curr)
        
        return True
