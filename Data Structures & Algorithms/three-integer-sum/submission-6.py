class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        output = []
        n = len(nums)
        i = 0
        while i < n - 2:
            tmp = nums[i]
            j = i + 1
            k = n - 1

            while i < n - 2 and nums[i+1] == nums[i]:
                i += 1

            while j < k:
                curr = tmp + nums[j] + nums[k]

                if curr == 0:
                    output.append([nums[i], nums[j], nums[k]])

                    # -4, -1, -1, 0, 1, 2

                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1

                    j += 1
                    k -= 1

                elif curr < 0:
                    j += 1
                elif curr > 0:
                    k -= 1
            
            i += 1
        
        # ans = []
        # for o in output:
        #     ans.append([o[0], o[1], o[2]])
            
        # print(ans)
        return output