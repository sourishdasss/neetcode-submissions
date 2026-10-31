import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        ans = r

        while l <= r:
            m = (l + r) // 2

            # check how long it takes
            tmp = 0
            for p in piles:
                tmp += math.ceil(float(p) / m)
            
            if tmp > h:
                l = m + 1
            else:
                ans = min(ans, m)
                r = m - 1
        
        return ans
        