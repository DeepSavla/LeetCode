class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Initially each node will be its patent
        # we have 1 to n nodes
        parent = []
        for i in range(len(edges) + 1):
            parent.append(i)
        # initially all have rank 1

        rank = [1] * (len(edges) + 1)

        # To find if they have same parents
        # If yes, then they are already connected so return false
        def find(n):
            p = parent[n]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        # return False if cant complete union
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
    
        # calling the union function
        for e in edges:
            if union(e[0], e[1]) == False:
                return e