class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_count = [0] * numCourses

        for p in prerequisites:
            # build adjacency list
            course = p[0]
            prereq = p[1]
            graph[prereq].append(course)

            # build in_count
            in_count[course] += 1

        # build queue
        queue = deque()
        for idx, val in enumerate(in_count):
            if val == 0:
                queue.append(idx)
        
        # kahn's algorithm
        while queue:
            node = queue.pop()
            children = graph[node]

            for c in children:
                in_count[c] -= 1
                if in_count[c] == 0:
                    queue.append(c)
            
        for i in in_count:
            if i > 0:
                return False

        return True