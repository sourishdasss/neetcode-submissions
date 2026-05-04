class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        start = 0

        if n == 0:
            return 0
            
        contains = set()
        contains.add(s[start])
        ans = 1

        # run a sliding window
        for end in range(1, n):
            # check if s[end] is already in contains set
            curr = s[end]
            while curr in contains:
                contains.remove(s[start])
                start += 1

            contains.add(curr)
            
            ans = max(ans, end - start + 1)
        
        return ans
