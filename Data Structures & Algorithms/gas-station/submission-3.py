class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [0] * n

        for i in range(n):
            diff[i] = gas[i] - cost[i]
        
        # test if impossible
        total = 0
        for i in range(n):
            total += diff[i]

        if total < 0:
            return -1
        
        print(diff)

        total = 0
        station = 0
        for i in range(n):
            total += diff[i]

            if total < 0:
                total = 0
                station = i + 1
        
        return station

