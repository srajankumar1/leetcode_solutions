class Solution:
    def coinChange(self, coins, amount):
        INF=10**9
        dp=[INF]*(amount+1)
        dp[0]=0
        for coin in coins:
            for i in range(coin,amount+1):
                if dp[i-coin]+1<dp[i]:
                    dp[i]=dp[i-coin]+1
        if dp[amount]==INF:
            return -1
        else:
            return dp[amount]