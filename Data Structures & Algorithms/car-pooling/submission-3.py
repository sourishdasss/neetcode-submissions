class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = defaultdict(list)

        for n, s, e in trips:
            events[s].append(-n)
            events[e].append(n)

        print(events.items())

        # sort by time
        sorted_events = sorted(list(events.items()))

        print(sorted_events)

        # iterate over the capacity
        currCapacity = capacity

        for _, pass_arr in sorted_events:
            print(pass_arr)

            for p in pass_arr:
                currCapacity += p

                print(currCapacity)
            
            if currCapacity < 0:
                return False

        return True
