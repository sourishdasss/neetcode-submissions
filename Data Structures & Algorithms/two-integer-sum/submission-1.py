class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for index, num in enumerate(nums):
            if num in diff:
                return [diff[num], index]
            else:
                curr_diff = target - num
                diff[curr_diff] = index
        