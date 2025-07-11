class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        grid = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    grid[i][j]=1
                else:
                    grid[i][j] = grid[i-1][j]+grid[i][j-1]
        
        return grid[m-1][n-1]


        # sc is O(N)
        # dp = [1] * n

        # for i in range(1,m):
        #     for j in range(1,n):
        #         dp[j] = dp[j] + dp[j-1]
        
        # return dp[-1]

        