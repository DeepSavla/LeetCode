class Solution:
    def DFS(self, node, visited, adj):
            visited[node] =True
            for n in adj[node]:
                if visited[n] == False:
                    self.DFS(n,visited, adj)
    
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = []
        visited = [False]* n
        components=0
        #creating adj
        for i in range(n):
            adj.append([])
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        #adj created
        for i in range(len(adj)):
            if visited[i] == False:
                components +=1
                self.DFS(i,visited,adj)
        return components
        
                
        
    
            
            