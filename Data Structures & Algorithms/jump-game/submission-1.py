class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        i = len(nums) - 1

        while i >= 0:
            dist = goal - i
            if nums[i] >= dist:
                goal = i
            i -= 1
        
        return True if goal == 0 else False

