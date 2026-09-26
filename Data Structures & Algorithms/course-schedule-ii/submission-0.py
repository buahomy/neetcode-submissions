class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        for dst, src in prerequisites:
            adj[src].append(dst)

        in_degree = [0] * numCourses
        for node in range(numCourses):
            for to in adj[node]:
                in_degree[to] += 1

        q = deque()
        for node in range(numCourses):
            if in_degree[node] == 0:
                q.append(node)

        topo_order = [0] * numCourses
        index_topo_node = 0
        while q:
            topo_node = q.popleft()
            topo_order[index_topo_node] = topo_node
            index_topo_node += 1

            for to in adj[topo_node]:
                in_degree[to] -= 1
                if in_degree[to] == 0:
                    q.append(to)

        return topo_order if index_topo_node == numCourses else []
