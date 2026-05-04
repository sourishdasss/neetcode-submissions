class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = defaultdict(int)
        for c in s:
            s_dict[c] += 1

        t_dict = defaultdict(int)
        for c in t:
            t_dict[c] += 1

        for c in s_dict:
            tmp = s_dict[c]
            if tmp != t_dict[c]:
                return False
        
        return True
        
