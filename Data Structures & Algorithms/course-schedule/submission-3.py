class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        self.graph = {}
        self.res = 0

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
                return False

        return len(black) == numCourses

    
    def dfs(self, crs, grey, black):
        grey.add(crs)

        for pre in self.graph[crs]:
            if pre in grey:
                return False
            if not self.dfs(pre, grey, black):
                return False
        
        grey.remove(crs)
        black.add(crs)

        return True











