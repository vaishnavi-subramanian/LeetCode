class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r,l=0,1
        maxp=0
        while l < len(prices):
            if prices[r]<prices[l]:
                profit=prices[l]-prices[r]
                maxp=max(maxp,profit)
            else:
                r=l
            l=l+1
        return maxp