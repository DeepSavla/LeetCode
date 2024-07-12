class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj =[]
        visited = [False] * n
        for i in range(n):
            adj.append([])
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        print(adj)
        def dfs(cur,parent):
            print(cur)
            visited[cur] = True
            for i in adj[cur]:
                if visited[i] ==False:
                    if dfs(i,cur) == False:
                        return False
                else:
                    if i!=parent:
                        return False
            return True
        if dfs(0,-1) == False:
            return False
        print(visited)
        for v in visited:
            if v==False:
                return False
        return True
                
        