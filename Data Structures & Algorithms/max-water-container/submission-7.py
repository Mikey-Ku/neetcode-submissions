class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        most = 0

        while L < R:
            water = (R-L) * min(heights[L], heights[R])
            most = max(water, most)

            if heights[L] < heights[R]:
                L += 1
            elif heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
        return most