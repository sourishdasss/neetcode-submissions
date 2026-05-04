class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row_count = len(grid)
        col_count = len(grid[0])

        dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            visited = set()
            distance = 0

            while queue:
                # process one full level
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    visited.add((r, c))

                    for dr, dc in dirs.values():
                        new_r, new_c = r + dr, c + dc

                        if 0 <= new_r < row_count and 0 <= new_c < col_count:
                            if (new_r, new_c) not in visited and grid[new_r][new_c] > 0:
                                if grid[new_r][new_c] > distance + 1:
                                    grid[new_r][new_c] = distance + 1
                                    queue.append((new_r, new_c))
                                    
                distance += 1

        for r in range(row_count):
            for c in range(col_count):
                if grid[r][c] == 0:
                    bfs(r, c)