class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        ans = 0

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))

            while queue:
                r, c = queue.popleft()
                visited.add((r, c))

                for d in dirs:
                    tmp_r, tmp_c = r + d[0], c + d[1]
                    if (tmp_r in range(rows) and tmp_c in range(cols) and grid[r][c] == '1' and (tmp_r, tmp_c) not in visited):
                        queue.append((tmp_r, tmp_c))
                        visited.add((r, c))

            return 1



        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == '1':
                    ans += bfs(r, c)

        return ans
