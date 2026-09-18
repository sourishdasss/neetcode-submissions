class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_len = math.inf
        
        for s in strs:
            max_len = min(max_len, len(s))

        i = 0
        output = ""

        print(max_len)

        while i < max_len:
            base = strs[0][i]
            for s in strs:

                print(base)
                if s[i] != base:
                    return output

            output += strs[0][i]
            i += 1

        return output