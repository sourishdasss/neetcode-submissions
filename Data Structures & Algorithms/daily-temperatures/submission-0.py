class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            print(i, t)
            while stack and t > stack[-1][1]:
                tmp = stack[-1][0]
                ans[tmp] = i - stack[-1][0]
                stack.pop()
            stack.append((i, t))
        
        return ans