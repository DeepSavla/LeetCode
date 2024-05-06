class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adjMat =[]
        for i in range(numCourses):
            adjMat.append([])
        for edge in prerequisites:
            adjMat[edge[1]].append(edge[0])
        for i in adjMat:
            for j in i:
                indegree[j] += 1
        q= deque()
        # till now first created adjMatrix followed by indegree of nodes
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        if len(q)==0:
            return False
        countQNodes = 0         #for cycle
        while len(q)!=0:
            s = q.popleft()
            for n in adjMat[s]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
            countQNodes +=1     #counting number of Nodes processed in queue
        if countQNodes == numCourses : #if all nodes have become 0 and entered queue
            return True
        else:
            return False
            