class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Initialize adjacency list as a dictionary with each character as a key and an empty set as the value
        # each key in the words is character, and its value will be a set of characters that are directly dependent on it (i.e., must come after it in the alien language order)
        adj = {}
        for w in words:
            for c in w:
                adj[c] = set()

        # Build the adjacency list based on the order in the words list
        for i in range(len(words) - 1):  # Compare each word with the next one
            w1 = words[i]
            w2 = words[i + 1]
            minLen = min(len(w1), len(w2))

            # Check if the prefix of the longer word matches the shorter word(invalid case)
            if len(w1) > len(w2) and w1[:minLen] == w2:
                return ""  # Invalid order

            # Find the first differing character between w1 and w2
            for j in range(minLen):
                if w1[j] != w2[j]:  # Characters differ
                    adj[w1[j]].add(w2[j])  # Add dependency: w1[j] must come before w2[j]
                    break  # Stop further comparisons after the first difference

        # Dictionary to track visitation state of each character
        visit = {}  # False = visited, True = currently path (cycle detection), not present: not yet visited
        res = []  # List to store the topological order of characters

        # Helper function for Depth-First Search (DFS) i.e. post-order DFS
        def dfs(c):
            if c in visit:  # If already visited
                return visit[c]  # Return whether it is currently visiting (detect cycle)

            visit[c] = True  # Mark as currently visiting
            for n in adj[c]:  # Traverse all neighbors
                if dfs(n):  # If a cycle is detected in the neighbor
                    return True

            visit[c] = False  # Mark as fully visited
            res.append(c)  # Add character to result after processing all neighbors

        # Perform DFS for each character in the adjacency list
        for c in adj:
            if dfs(c):  # If a cycle is detected, return empty string
                return ""

        # Reverse the result list to get the correct topological order
        res.reverse()
        return "".join(res)  # Join the characters to form the result string