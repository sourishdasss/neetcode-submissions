class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for i in range(len(nums) - 2):
            # if nums[i] > 0:
            #     break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            start = i + 1
            end = len(nums) - 1
            while start < end:
                tmp_sum = nums[i] + nums[start] + nums[end]
                if tmp_sum < 0:
                    start += 1
                elif tmp_sum > 0:
                    end -= 1
                else:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1
        
        return result
                    
                    




        