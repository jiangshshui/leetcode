class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp=[False for _ in range(len(s)+1)]
        #dp[j] 表示s[0...j-1]在wordDict中
        dp[0]=True
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and wordDict.count(s[j:i])!=0:
                    dp[i]=True
                    break
        return dp[len(s)]

s=Solution()
print(s.wordBreak("leetcode",["leet","code"]))