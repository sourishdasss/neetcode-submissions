class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        curr = 0

        while curr < len(nums):
            if nums[curr] == 0:
                ahead = curr + 1
                while ahead < len(nums) and nums[curr] == nums[ahead]:
                    ahead += 1
                
                # perform the swap
                if ahead < len(nums):
                    tmp = nums[curr]
                    nums[curr] = nums[ahead]
                    nums[ahead] = tmp
            
            curr += 1