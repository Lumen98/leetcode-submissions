class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        if  numCourses == 0:
            return []
        if not prerequisites:
            return [i for i in range(numCourses)]

        self.graph = {}
        self.res = []

        for i in range(numCourses):
            self.graph[i] = []
        
        for crs, pre in prerequisites:
            self.graph[crs].append(pre)
        
        white = set(self.graph.keys())
        self.grey = set()
        self.black = set()

        while white:
            curr = white.pop()
            
            if curr not in self.black:
                
                if not self.dfs(curr):
                    return []
            
        return self.res

    def dfs(self, crs):
        self.grey.add(crs)

        for nei in self.graph[crs]:
            if nei in self.grey:
                return False
            if nei in self.black:
                continue
            if not self.dfs(nei):
                return False

        self.grey.remove(crs)
        self.res.append(crs)
        self.black.add(crs)

        return True


