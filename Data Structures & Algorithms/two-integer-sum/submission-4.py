class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        ans = []

        for i, n in enumerate(nums):
            diff = target - n
            print(diff)

            if n in diff_map:
                ans = [diff_map[n], i]
                break
            else:
                diff_map[diff] = i

        return ans
            
            