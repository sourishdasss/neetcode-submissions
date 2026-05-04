class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        rows = len(grid)
        cols = len(grid[0])

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def in_bounds(curr, limit):
            if curr >= 0 and curr < limit:
                return True
            return False

        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))

            while queue:
                curr_r, curr_c = queue.popleft()
                for d in dirs:
                    move_r, move_c = d

                    new_r = curr_r + move_r
                    new_c = curr_c + move_c

                    if in_bounds(new_r, rows) and in_bounds(new_c, cols):
                        if grid[new_r][new_c] == "1" and (new_r, new_c) not in visited:
                            visited.add((new_r, new_c))
                            queue.append((new_r, new_c))

            return 1

        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += bfs(r, c)

        return islands


