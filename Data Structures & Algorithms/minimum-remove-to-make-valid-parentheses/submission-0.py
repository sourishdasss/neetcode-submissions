class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        indices_to_remove = set()

        for i, c in enumerate(s):
            if c == "(":
                stack.append([c, i])
            elif c == ")":
                if stack and stack[-1][0] == "(":
                    stack.pop()
                else:
                    indices_to_remove.add(i)

        # if stack not empty we need to remove those indices
        for c, i in stack:
            indices_to_remove.add(i)

        print(indices_to_remove)
        
        # remove the indices_to_remove from the string
        result = ""
        for i, c in enumerate(s):
            if i not in indices_to_remove:
                result += c
        
        return result
