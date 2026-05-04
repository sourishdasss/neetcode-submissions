class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        ans = []

        for index, n in enumerate(nums):
            complement = target - n

            if complement in diff:
                return [diff[complement], index]

            diff[n] = index