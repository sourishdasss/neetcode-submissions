class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        n = len(grid)
        m = len(grid[0])
        
        dirs = {
            "u": (-1, 0),
            "d": (1, 0),
            "l": (0, -1),
            "r": (0, 1)
        }
        
        def bfs(i, j):
            q = deque([(i, j)])
            visited.add((i, j))

            while q:
                i, j = q.popleft()

                # add neighbours
                for _, d in dirs.items():
                    v, h = d
                    new_i, new_j = i + v, j + h

                    # check if alr visited and in bounds
                    if (new_i, new_j) not in visited:
                        if new_i > -1 and new_i < n:
                            if new_j > -1 and new_j < m:
                                if grid[new_i][new_j] == '1':
                                    q.append((new_i, new_j))   
                                    visited.add((new_i, new_j))  

        # find any land
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    # check if already visited
                    if (i, j) in visited:
                        continue
                    else:
                        count += 1
                        bfs(i, j)

        return count