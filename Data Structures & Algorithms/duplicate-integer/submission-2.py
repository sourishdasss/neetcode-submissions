class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = defaultdict(int)

        for n in nums:
            dic[n] += 1

            if dic[n] > 1:
                return True

        return False