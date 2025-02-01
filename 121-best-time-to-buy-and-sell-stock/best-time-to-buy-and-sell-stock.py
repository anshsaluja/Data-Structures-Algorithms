class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
       
        minprices = prices[0]
        maxi = 0

        for i in range(len(prices)):
            minprices = min(prices[i], minprices)
            p = prices[i]-minprices
            maxi = max(maxi,p)
        
        return maxi



        # minprice = prices[0]
        # maxp = 0

        # for i in range(len(prices)):
        #     minprice = min(minprice, prices[i])
        #     p = prices[i]-minprice
        #     maxp = max(maxp,p)

        # return maxp
        