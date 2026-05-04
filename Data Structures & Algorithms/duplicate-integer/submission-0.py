class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_map = {}

        for i in nums:
            if i in nums_map:
                return True
            else:
                nums_map[i] = 1
        
        return False


         