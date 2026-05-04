class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        exclude_first = nums[1:]
        exclude_last = nums[:-1]

        print(exclude_first, exclude_last)

        # run house robber 1 on each array and take max
        dp_1 = [0] * len(exclude_first)
        dp_2 = [0] * len(exclude_last)

        dp_1[0] = exclude_first[0]
        dp_2[0] = exclude_last[0]

        if len(nums) > 2:
            dp_1[1] = max(exclude_first[0], exclude_first[1])
            dp_2[1] = max(exclude_last[0], exclude_first[1])

            for i in range(2, len(exclude_first)):
                tmp = dp_1[i-2] + exclude_first[i]
                dp_1[i] = max(dp_1[i-1], tmp)

            for i in range(2, len(exclude_last)):
                tmp = dp_2[i-2] + exclude_last[i]
                dp_2[i] = max(dp_2[i-1], tmp)
        
        print(dp_1, dp_2)

        return max(dp_1[-1], dp_2[-1])
