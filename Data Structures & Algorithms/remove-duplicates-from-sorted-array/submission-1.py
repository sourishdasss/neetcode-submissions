class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = defaultdict(int)
        for n in nums:
            unique[n] += 1

        keys = list(unique.keys())
        print(keys)
        ans = len(keys)
        for i in range(ans):
            nums[i] = keys[i]

        return ans