class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = []
        visited = [False] *n
        for i in range(n):
            adj.append([])
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        def dfsTraverse(source,parent):
            visited[source]=True
            for n in adj[source]:
                if visited[n] ==False:
                    if dfsTraverse(n,source):
                        return True
                else:
                    if n!=parent:
                        return True
            return False
        
        if dfsTraverse(i,-1)==True:
                    return False
        for i in range(n):
            if visited[i]==False:
                return False
        return True
            
        