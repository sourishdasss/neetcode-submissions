class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            a = s[start]
            b = s[end]

            # check if inner combinations are valid
            if a != b:
                remove_left = s[start+1:end+1]
                remove_right = s[start:end]

                # check if either of them are valid
                if remove_left == remove_left[::-1] or remove_right == remove_right[::-1]:
                    return True
                else:
                    return False
            else:
                start += 1
                end -= 1
        
        return True