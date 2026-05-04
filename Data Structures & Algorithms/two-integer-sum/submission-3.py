class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        ans = []

        for i, n in enumerate(nums):
            curr_diff = target - n
            print(curr_diff)

            if curr_diff in diff:
                ans = [diff[curr_diff], i]
            else:
                diff[n] = i
        
        print(diff)
        return ans