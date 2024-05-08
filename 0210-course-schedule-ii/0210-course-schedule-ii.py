class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = []
        outputOrder = []
        q=deque()
        for i in range(numCourses):
            adj.append([])
        for p in prerequisites:
            adj[p[1]].append(p[0])
        degree = [0] * numCourses
        for i in adj:
            for j in i:
                degree[j] +=1
        #found adjMat and inDegree
        for i in range(len(degree)):
            if degree[i] == 0:
                q.append(i)
        while len(q) !=0:
            s=q.popleft()
            outputOrder.append(s)
            for n in adj[s]:
                degree[n] -=1
                if degree[n] ==0:
                    q.append(n)
        if len(outputOrder) == numCourses:
            return outputOrder
        else:
            return []
        
                