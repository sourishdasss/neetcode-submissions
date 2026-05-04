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

        gas_in_tank = 0
        station = 0
        for i in range(n):
            gas_in_tank += diff[i]

            # if we ever reach negative, that station isn't possible
            if gas_in_tank < 0:
                gas_in_tank = 0
                station = i + 1
        
        return station

