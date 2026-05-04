class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        neq = n

        if n == 1:
            if nums[l] == val:
                neq -= 1

        while l < r:
            if nums[l] == val:
                print('here', l , r)
                while r > l and nums[r] == val:
                    r -= 1
                    neq -= 1
                tmp = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp
                r -= 1
                neq -= 1
            l += 1
        print(neq)
        
        return neq
        
