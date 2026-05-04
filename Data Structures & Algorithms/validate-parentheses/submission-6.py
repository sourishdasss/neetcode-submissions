from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matching = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s:
            if c in matching:
                tmp = matching[c]
                if len(stack) > 0 and stack[-1] == tmp:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
            print(c, stack)

        return len(stack) == 0