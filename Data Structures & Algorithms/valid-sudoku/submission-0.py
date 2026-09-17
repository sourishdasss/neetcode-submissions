class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we will be going row by row, so no need to have a persistant hash map pe row, just have one for each col and grid

        col_dict = defaultdict(lambda: defaultdict(int))
        grid_dict = defaultdict(lambda: defaultdict(int))

        print(2 // 3)

        for i, r in enumerate(board):
            row_dict = defaultdict(int)

            for j, c in enumerate(r):
                #print(grid_dict.items())

                # skip if blank
                if c == ".":
                    continue

                # add to row dict if valid
                if row_dict[c] == 0:
                    row_dict[c] += 1
                else:
                    print("row", (i, j))
                    return False

                # add to col dict
                if col_dict[j][c] == 0:
                    col_dict[j][c] += 1
                else:
                    print("col", (i, j))
                    return False

                # add to grid dict

                # hash to correct key
                hashed_i = i // 3
                hashed_j = j // 3

                print("grid", (i, j), (hashed_i, hashed_j), c)

                if grid_dict[(hashed_i, hashed_j)][c] == 0:
                    grid_dict[(hashed_i, hashed_j)][c] += 1
                else:
                    print("grid", (i, j), (hashed_i, hashed_j), c)
                    print(grid_dict.items())
                    return False
        
        return True
