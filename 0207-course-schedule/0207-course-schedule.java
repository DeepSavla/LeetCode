class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // Step 1: Create an indegree array to track number of incoming edges for each course
        int[] indegree = new int[numCourses];
        // Step 2: Create an adjacency list to represent the graph
        List<List<Integer>> adj = new ArrayList<>(numCourses);
        // Initialize the adjacency list with empty lists for each course
        for (int i = 0; i < numCourses; i++) {
            adj.add(new ArrayList<>());
        }
        // Step 3: Build the graph from the prerequisites
        for (int[] prerequisite : prerequisites) {
            int course = prerequisite[0];
            int dependency = prerequisite[1];
            // dependency -> course
            adj.get(dependency).add(course); // Add edge to adjacency list
            indegree[course]++;              // Increase indegree of the course
        }
        // Step 4: Initialize the queue with all courses having 0 indegree (no prerequisites)
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }
        // Step 5: Process nodes using BFS (Kahn's Algorithm)
        int nodesVisited = 0;
        while (!queue.isEmpty()) {
            int node = queue.poll(); // Remove a node with indegree 0
            nodesVisited++;          // Count the course as completed
            // Visit all the neighbors (courses that depend on current course)
            for (int neighbor : adj.get(node)) {
                indegree[neighbor]--; // Remove the edge
                // If neighbor now has no prerequisites, add it to the queue
                if (indegree[neighbor] == 0) {
                    queue.offer(neighbor);
                }
            }
        }
        // Step 6: If we've visited all courses, we can finish all
        return nodesVisited == numCourses;
    }
}
