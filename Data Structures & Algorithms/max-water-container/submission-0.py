class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        maximum = 0
        while L < R:
            width = R - L
            height = min(heights[L],heights[R])
            if (width * height) > maximum:
                maximum = width * height
            if heights[L] <= heights[R]:
                L+=1
            elif heights[L] > heights[R]:
                R-=1

        return maximum

        