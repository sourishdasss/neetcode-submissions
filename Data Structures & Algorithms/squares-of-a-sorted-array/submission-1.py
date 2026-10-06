class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # use a 2 pointer approach
        l = 0
        r = len(nums) - 1

        out = []

        while l <= r:
            l_num = abs(nums[l])
            r_num = abs(nums[r])

            if r_num > l_num:
                out.append(r_num * r_num)
                r -= 1
            else:
                out.append(l_num * l_num)
                l += 1

        out.reverse()
        
        return out