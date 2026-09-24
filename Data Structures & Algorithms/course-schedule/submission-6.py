class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites:
            return True
        
        self.graph = {}

        for i in range(numCourses):
            self.graph[i] = []
        
        for crs, pre in prerequisites:
            self.graph[crs].append(pre)
        
        self.grey = set()
        self.black = set()

        white = set(self.graph.keys())

        while white:
            curr = white.pop()

            if not self.dfs(prerequisites, curr):
                return False
            

        return len(self.black) == numCourses



    def dfs(self, prerequisites, course):
        
        self.grey.add(course)

        for pre in self.graph[course]:
            
            if pre in self.grey:
                return False
            if course in self.black:
                continue
            if not self.dfs(prerequisites, pre):
                return False
        
        self.grey.remove(course)
        self.black.add(course)

        return True







        