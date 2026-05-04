class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        output = set()
        n = len(nums)
        i = 0
        while i < n - 2:
            tmp = nums[i]
            j = i + 1
            k = n - 1

            while j < k:
                curr = tmp + nums[j] + nums[k]

                if curr == 0:
                    output.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif curr < 0:
                    j += 1
                elif curr > 0:
                    k -= 1
            
            i += 1
        
        ans = []
        for o in output:
            ans.append([o[0], o[1], o[2]])
            
        print(ans)
        return ans