class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        """
        maxDiff=0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                maxDiff = max(maxDiff, prices[j]-prices[i])
        return maxDiff
        """
        maxProfit = 0
        profitIfSoldToday = 0
        leastValue = prices[0]
        for i in range(len(prices)):
            if prices[i]<leastValue:
                leastValue = prices[i]
            profitIfSoldToday = prices[i] - leastValue
            maxProfit = max(maxProfit,profitIfSoldToday)
        return maxProfit
        
            
              