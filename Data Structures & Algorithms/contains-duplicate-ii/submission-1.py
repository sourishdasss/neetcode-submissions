class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = defaultdict(int)

        start = 0
        end = k


        for i in range(min(len(nums), end + 1)):
            curr_num = nums[i]
            freq[curr_num] += 1

            if freq[curr_num] > 1:
                return True

        while end < len(nums) - 1:
            start_num = nums[start]
            freq[start_num] -= 1
            start += 1

            end += 1
            end_num = nums[end]
            freq[end_num] += 1


            if freq[end_num] > 1:
                return True 
        
        return False



