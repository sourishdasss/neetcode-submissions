class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]

        # test if impossible
        total = sum(diff)
        if total < 0:
            return -1
        
        gas_in_tank = 0
        station = 0
        for i in range(n):
            gas_in_tank += diff[i]

            # if we ever reach negative, that station isn't possible
            if gas_in_tank < 0:
                gas_in_tank = 0
                station = i + 1
        
        return station

