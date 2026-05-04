class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def coord_in_range(coords, move, grid):
            rows = len(grid)
            cols = len(grid[0])
            new_coord = (coords[0] + move[0], coords[1] + move[1])

            if new_coord[0] >= 0 and new_coord[0] < rows:
                if new_coord[1] >= 0 and new_coord[1] < cols:
                    return True
            
            return False


        # BFS Algorithm for a graph
        def bfs(coords, grid, visited):
            row = coords[0]
            col = coords[1]

            queue = collections.deque()
            queue.append(coords)

            curr_island_size = 0
            curr_island = set()

            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                coords = queue.popleft()
                curr_island.add(coords)
                for move in moves:
                    # Check if new coordinate is in grid
                    if coord_in_range(coords, move, grid):
                        new_coord = (coords[0] + move[0], coords[1] + move[1])
                        if grid[new_coord[0]][new_coord[1]] == 1 and new_coord not in visited:
                            queue.append(new_coord)
                            visited.add(new_coord)
                            curr_island.add(new_coord)
                            curr_island_size += 1
            
            return len(curr_island)


        rows = len(grid)
        cols = len(grid[0])
        visited_coords = set()

        max_size = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited_coords:
                    max_size = max(max_size, bfs((row, col), grid, visited_coords))

        return max_size

