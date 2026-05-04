class Solution:
    def isPalindrome(self, s: str) -> bool:
        def remove_invalid_characters(s: str) -> str:
            new_s = ''
            for c in s:
                if (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('0') and ord(c) <= ord('9')):
                    new_s += c
            return new_s

        # clean text
        s = s.lower()
        s = remove_invalid_characters(s)
        print(s)

        # run two pointer algorithm
        start = 0
        end = len(s) - 1

        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True

        