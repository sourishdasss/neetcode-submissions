class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1
        max_water = 0

        while l < r:
            width = r - l

            curr_water = width * min(heights[l], heights[r])
            max_water = max(curr_water, max_water)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_water



        