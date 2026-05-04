class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []

        def dfs(curr_sel, curr):
            # check if we have no more values to pick from
            if len(curr) == len(nums):
                perms.append(curr.copy())
                return
            
            for i in range(len(curr_sel)):
                if curr_sel[i] == True:
                    new_sel = curr_sel.copy()
                    new_sel[i] = False
                    dfs(new_sel, curr + [nums[i]])

        curr_sel = [True] * len(nums)
        dfs(curr_sel, [])

        return perms
