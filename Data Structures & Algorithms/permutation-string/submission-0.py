class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = sorted(s1)
        start = 0
        end = len(s1) - 1
        s2_len = len(s2)

        print(start, end, s1)

        def isPerm(s1, start, end, s2):
            tmp_substring = []
            while start <= end:
                tmp_substring += (s2[start])
                start += 1
            
            print(tmp_substring, s1)
            
            if s1 == sorted(tmp_substring):
                return True
            

        while end < s2_len:
            if isPerm(sorted(s1), start, end, s2):
                return True
            end += 1
            start += 1

        return False