class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjacency list
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for u, v in prerequisites:
            graph[u].append(v)
            in_degree[v] += 1

        # find starting courses
        queue = deque([])

        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        count = 0

        while queue:
            curr = queue.popleft()
            neighbours = graph[curr]

            for n in neighbours:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    queue.append(n)

        print(count)

        print(in_degree)

        for u in in_degree:
            if u != 0:
                return False

        return True

        
        