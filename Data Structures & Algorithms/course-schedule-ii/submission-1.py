class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        order = []

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        # finding starting nodes
        starting_nodes = []
        for i, d in enumerate(in_degree):
            if d == 0: 
                 starting_nodes.append(i)

        print(starting_nodes)
        
        # start bfs
        queue = deque(starting_nodes)


        while queue:
            node = queue.popleft()
            neighbours = graph[node]
            for n in neighbours:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    queue.append(n)
            order.append(node)

        return order if len(order) == numCourses else []


        