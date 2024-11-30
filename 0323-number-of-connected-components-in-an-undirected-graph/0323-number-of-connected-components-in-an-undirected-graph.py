class Solution:
    def DFS(self, node, visited, adj):
            visited[node] =True
            for n in adj[node]:
                if visited[n] == False:
                    self.DFS(n,visited, adj)
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = []
        for i in range(n):
            adj.append([])
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
            
        visited = [False]* n
        components = 0
        for i in range(len(adj)):
            if visited[i] == False:
                components +=1
                self.DFS(i,visited,adj)
        return components
        
'''
- Using DFS
- create adjcency list using the edges
- Create a visited array to track nodes visited through each DFS call
- for all the nodes if they are not visited, perform recursive DFS
- DFC at outer level will be performed the number of times as the number of disconnected components (connected nodes will be visited through the internal DFS)

'''