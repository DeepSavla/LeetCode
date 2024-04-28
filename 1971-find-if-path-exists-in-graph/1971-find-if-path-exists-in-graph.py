class Solution:
    def createAdj(self, n, edges):
        adj = []
        for i in range(n):
            adj.append([])
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        return adj
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        adj = self.createAdj(n, edges)
        visited = [False]*n
        q=deque()
        q.append(source)
        visited[source] = True
        while len(q)!=0:
            source = q[0]
            q.popleft()
            for node in adj[source]:
                if node == destination:
                    return True
                if visited[node] ==False:
                    q.append(node)
                    visited[node] = True
            
        