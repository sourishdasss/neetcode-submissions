class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_fruit = 0
        rn = len(grid)
        cn = len(grid[0])

        q = deque([])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh_fruit += 1
                elif grid[row][col] == 2:
                    q.append((row, col, 0))

        # check if we start with no fresh fruit
        if fresh_fruit == 0:
            return 0

        dirs = {
            "up" : (-1, 0),
            "down" : (1, 0),
            "left" : (0, -1),
            "right" : (0, 1)
        }

        finish_time = 0
        
        # run bfs
        while q:
            r, c, t = q.popleft()

            # check neighbours
            for d in dirs.values():
                nr, nc, nt = r + d[0], c + d[1], t + 1

                # check if in-bounds
                if nr > -1 and nr < rn:
                    if nc > -1 and nc < cn:
                        # check for fresh fruit
                        if grid[nr][nc] == 1:
                            q.append((nr, nc, nt))
                            grid[nr][nc] = 2
                            fresh_fruit -= 1

                            finish_time = max(finish_time, nt)

        if fresh_fruit == 0:
            return finish_time
        else:
            return -1
                

                


