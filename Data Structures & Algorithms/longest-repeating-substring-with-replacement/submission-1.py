class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        count = [0] * 26

        l = 0
        longest = 0
        for r in range(n):
            count[ord(s[r]) - ord('A')] += 1

            # check if there are enough replacements
            if r - l + 1 - max(count) > k:
                print('here', l, r)
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
                print('here', l, r)
            
            longest = max(longest, r - l + 1)
        
        return longest
            

