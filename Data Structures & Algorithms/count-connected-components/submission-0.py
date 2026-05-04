class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # run bfs
        visited = set()
        count = 0

        for i in range(n):
            if i not in visited:
                q = deque([])
                q.append(i)
                visited.add(i)

                while q:
                    curr = q.popleft()

                    neighbours = graph[curr]
                    for n in neighbours:
                        if n not in visited:
                            visited.add(n)
                            q.append(n)

                count += 1
        
        return count




