import bisect

class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

        print(self.timemap)

    def get(self, key: str, timestamp: int) -> str:
        curr_arr = self.timemap[key]

        # run binary search to get most recent timestamp
        index = bisect.bisect_left(curr_arr, (timestamp, "zzz"))

        print(index)

        if index == 0:
            return ""
        elif index == len(curr_arr):
            return curr_arr[index-1][1]
        else:
            return curr_arr[index-1][1]
        
