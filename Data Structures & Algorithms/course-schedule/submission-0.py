class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #numCourse = nodes, prerequisites = edges(in-degree)
        in_degree = [0] * numCourses
        adj = defaultdict(list) # list-> value >> {_ : []}

        # dependencies & adjacency list
        for dest, src in prerequisites: # dest node/ source node
            adj[src].append(dest)
            in_degree[dest] += 1

        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0: 
                queue.append(i) #index to pop first

        finish = 0 #if in the end in_degree = 0 -> no cycle
        while queue:
            node = queue.popleft()
            finish += 1
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return finish == numCourses                       