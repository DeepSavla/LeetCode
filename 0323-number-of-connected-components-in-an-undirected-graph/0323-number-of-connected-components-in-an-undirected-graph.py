class Solution:
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
        def DFS(node):
            visited[node] =True
            for n in adj[node]:
                if visited[n] == False:
                    DFS(n)
        
        for i in range(len(adj)):
            if visited[i] == False:
                components +=1
                DFS(i)
        return components
        
                
        
    
            
            