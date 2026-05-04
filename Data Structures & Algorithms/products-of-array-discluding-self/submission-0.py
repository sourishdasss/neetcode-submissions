class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prev = [1] * n 
        forward = [1] * n

        for i in range(1, n):
            prev[i] = nums[i-1] * prev[i-1]
        
        for i in range(n-2, -1, -1):
            forward[i] = nums[i+1] * forward[i+1]

        ans = [0] * n
        for i in range(n):
            ans[i] = prev[i] * forward[i]
        
        return ans