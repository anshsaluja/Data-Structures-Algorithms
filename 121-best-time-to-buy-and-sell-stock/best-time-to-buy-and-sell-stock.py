class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
       
        minprices = prices[0]
        maxi = 0

        for i in range(len(prices)):
            minprices = min(minprices,prices[i])
            profit = prices[i]-minprices
            maxi = max(maxi,profit)

        
        return maxi