class Solution(object):
    def coinChange(self, coins, amount):
        if amount<=0:
            return 0
        max=2**31-1
        dp=[max for i in range(0,amount+1)]
        for item in coins:
            if item<=amount:
                dp[item]=1
        for i in range(1,amount+1):
            if dp[i]!=max:
                continue
            for j in range(1,len(coins)+1):
                if i-coins[j-1]>0:
                    dp[i]=min(dp[i],dp[i-coins[j-1]]+1)
        if dp[amount]==max:
            return -1
        else:
            return dp[amount]
s=Solution()
#print(s.coinChange([1,2,5],11))
print(s.coinChange([1],1))

