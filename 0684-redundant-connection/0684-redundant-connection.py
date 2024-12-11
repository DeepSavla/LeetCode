#build graph one edge at a time and check if there are cycles in graph
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def cycleExists(visited,node,source):
            for n in adj[node]:
                if n not in visited:
                    visited.add(n)
                    if cycleExists(visited,n,node):
                        return True
                elif n != source:
                    return True
            return False
        
        #creating adj list
        adj = []
        #since only one redundant edge 
        # hence, number of nodes = number of edges
        for i in range(len(edges)+1):
            adj.append([])
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
            visited = set()
            visited.add(e[0])
            if cycleExists(visited,e[0],e[1]):
                return e
        
        
            