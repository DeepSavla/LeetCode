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
        
        maxDiff=0
        i=0
        j=1
        while j<len(prices):
            if  prices[i] < prices[j]:
                maxDiff = max(maxDiff, prices[j]-prices[i])
            else:
                i=j
            j+=1
        return maxDiff
        """
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                max_profit =max(prices[right] - prices[left],max_profit)
            else:
                left = right
            right += 1
        return max_profit
        """
        
            
              