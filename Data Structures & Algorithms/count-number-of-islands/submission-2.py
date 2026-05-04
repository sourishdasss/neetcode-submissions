class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ans = 0

        dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

        row_count = len(grid)
        col_count = len(grid[0])

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()

                # debug
                print(row, col)

                visited.add((row, col))
                
                for d in dirs.values():
                    move_r, move_c = d

                    new_r = move_r + row
                    new_c = move_c + col

                    if 0 <= new_r < row_count:
                        if 0 <= new_c < col_count:
                            if (new_r, new_c) not in visited:
                                # check if it's land
                                if grid[new_r][new_c] == "1":
                                    queue.append((new_r, new_c))

            return 1
                    
        # run bfs
        for r in range(row_count):
            for c in range(col_count):
                if grid[r][c] == "1" and (r, c) not in visited:
                    ans += bfs(r, c)

        return ans



