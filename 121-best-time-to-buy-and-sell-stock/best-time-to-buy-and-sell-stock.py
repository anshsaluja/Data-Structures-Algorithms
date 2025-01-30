class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        minprice = prices[0]
        maxp = 0

        for i in range(len(prices)):
            minprice = min(minprice, prices[i])
            p = prices[i]-minprice
            maxp = max(maxp,p)

        return maxp
        