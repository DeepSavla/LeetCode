class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = []
        for i in range(n):
            adj.append([])
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        visited = [False] * n
        connectedComponents = 0
        
        def DFS(n, visited):
            for node in adj[n]:
                if visited[node] == False:
                    visited[node] = True
                    DFS(node,visited)
        
        for i in range(n):
            if visited[i] == False:
                connectedComponents +=1
                visited[i] = True
                DFS(i,visited)
        return connectedComponents
        
'''
- Using DFS
- create adjcency list using the edges
- Create a visited array to track nodes visited through each DFS call
- for all the nodes if they are not visited, perform recursive DFS
- DFC at outer level will be performed the number of times as the number of disconnected components (connected nodes will be visited through the internal DFS)

'''