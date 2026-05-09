class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallestSoFar = prices[0]
        ans = 0
        for i in range(1, len(prices), 1):
            if (smallestSoFar < prices[i]):
                ans = max(ans, prices[i]-smallestSoFar)
            else:
                smallestSoFar = prices[i]
            
        return ans
            

        