class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        ans = []

        for i, n in enumerate(nums):
            if n in diff:
                ans = [i, diff[n]]
            else:
                diff[target - n] = i

        ans.sort()

        return ans
        
