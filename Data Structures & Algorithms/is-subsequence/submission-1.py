class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pos = 0

        if not s:
            return True

        for t_char in t:
            s_char = s[s_pos]

            if s_char == t_char:
                s_pos += 1
            
                if s_pos == len(s):
                    return True

        return False