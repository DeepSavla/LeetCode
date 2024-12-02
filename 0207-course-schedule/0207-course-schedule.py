#detect cycle using DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = []
        for i in range(numCourses):
            adjList.append([])
        visited = [False]*numCourses
        cycleDetection = False
        for p in prerequisites:
            adjList[p[1]].append(p[0])
        cycleSet = set()
        cycleSet.add(0)
        def DFS(s):
            nonlocal cycleDetection
            cycleSet.add(s)
            for node in adjList[s]:
                if visited[node] == False:
                    visited[node] = True
                    DFS(node)
                elif node in cycleSet:
                    cycleDetection = True
                    return
            cycleSet.remove(s)
            
        
        for i in range(numCourses):
            if visited[i] == False:
                visited[i] = True
                DFS(i)
        if cycleDetection == True:
            return False
        return True
        
        