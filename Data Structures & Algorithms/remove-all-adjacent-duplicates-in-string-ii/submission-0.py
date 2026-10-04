class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            # check if matching characters
            if stack and c == stack[-1][0]:
                # check if the count is k
                tmp_count = stack[-1][1] + 1
                if tmp_count == k:
                    stack.pop()
                else:
                    stack.pop()
                    stack.append((c, tmp_count))
            else:
                stack.append((c, 1))

        output = ""
        for char, count in stack:
            for i in range(count):
                output += char
        
        return output