class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        for i in range(0, len(heights), 1):
            for j in range(i+1, len(heights), 1):
                ans = max(ans, (j-i)*min(heights[i], heights[j]))
        return ans