class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0

        for i in range(len(nums)):
            max_reachable = max(max_reachable, i + nums[i])

            print(max_reachable)

            if i != len(nums) - 1 and max_reachable < i + 1:
                return False
        
        return True
