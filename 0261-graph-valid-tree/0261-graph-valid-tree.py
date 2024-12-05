class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj =[]
        for i in range(n):
            adj.append([])
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        visited = [False]*n
        visited[0] = True
        cycle = False
        def DFS(source, parent):
            nonlocal cycle
            for node in adj[source]:
                if visited[node] == False:
                    visited[node] = True
                    DFS(node, source)
                elif node != parent:
                    cycle = True
        DFS(0,-1)
        for v in visited:
            if v==False:
                return False
        if cycle:
            return False
        else:
            return True
                
