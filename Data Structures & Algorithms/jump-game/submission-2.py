class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_jump = nums[0]

        print(max_jump)

        for i in range(1, n):
            print(i, max_jump)
            if i > max_jump:
                return False
            max_jump = max(max_jump, i + nums[i])
            
            # print(max_jump)
            # if i <= max_jump:
            #     return False


        
        return max_jump >= n - 1
