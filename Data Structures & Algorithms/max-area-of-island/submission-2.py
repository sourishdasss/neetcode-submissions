class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # if grid does not exist
        if not grid:
            return 0

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r, c) -> int:
            stack = [(r, c)]
            visited.add((r, c))
            curr_area = 0
            while stack:
                r, c = stack.pop()
                curr_area += 1
                for d in dirs:
                    tmp_r, tmp_c = r + d[0], c + d[1]
                    if tmp_r in range(rows) and tmp_c in range(cols) and (tmp_r, tmp_c) not in visited:
                        if grid[tmp_r][tmp_c] == 1:
                            stack.append((tmp_r, tmp_c))
                            visited.add((tmp_r, tmp_c))
            return curr_area

        for r in range(rows):
            for c in range(cols):
                # only run dfs if the coord hasn't been visited already
                if (r, c) not in visited and grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area


