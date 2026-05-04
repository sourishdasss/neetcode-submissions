class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        ans = 0
        contains = set()

        for r in range(len(s)):
            curr = s[r]

            # check for duplicates
            duplicate = curr in contains
            if duplicate:
                while curr in contains:
                    contains.remove(s[l])
                    l += 1

            contains.add(s[r])
            ans = max(ans, r - l + 1)
        
        return ans