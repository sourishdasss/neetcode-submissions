class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        forward = {
            "0" : "1",
            "1" : "2",
            "2" : "3",
            "3" : "4",
            "4" : "5",
            "5" : "6",
            "6" : "7",
            "7" : "8",
            "8" : "9",
            "9" : "0",
        }

        backward = {
            "0" : "9",
            "1" : "0",
            "2" : "1",
            "3" : "2",
            "4" : "3",
            "5" : "4",
            "6" : "5",
            "7" : "6",
            "8" : "7",
            "9" : "8",
        }
        
        
        q = deque([("0000", 0)])

        visited = set()
        for d in deadends:
            visited.add(d)

        if "0000" in visited:
            return -1
        
        visited.add("0000")

        while q:
            curr, moves = q.popleft()

            # find all neighbours
            for i in range(4):
                curr_char = curr[i]
                
                # forward
                forward_char = forward[curr_char]
                forward_tmp = curr[:i] + forward_char + curr[i+1:]

                # backward 
                backward_char = backward[curr_char]
                backward_tmp = curr[:i] + backward_char + curr[i+1:]

                # print(forward_tmp, backward_tmp)

                # check if we reached the target
                if forward_tmp == target:
                    return moves + 1

                if backward_tmp == target:
                    return moves + 1

                # add to queue
                if forward_tmp not in visited:
                    q.append((forward_tmp, moves + 1))
                    visited.add(forward_tmp)

                if backward_tmp not in visited:
                    q.append((backward_tmp, moves + 1))
                    visited.add(backward_tmp)

        return -1



                