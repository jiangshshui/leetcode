'''
    超时的方法。
'''
# class Solution(object):
#     def longestPalindrome(self,s):
#         length=len(s)
#         maxlength=0
#         start=0
#         for i in range(length):
#             for j in range(i,length,1):
#                 temp1=i
#                 temp2=j
#                 while temp1<=temp2 :
#                     if s[temp1]!=s[temp2]:
#                         break
#                     else:
#                         temp1+=1
#                         temp2-=1
#                 if temp1>=temp2 and j-i+1>maxlength:
#                     maxlength=j-i+1
#                     start=i
#         if maxlength>0:
#             return s[start:maxlength+start]
#         else:
#             return ""



# class Solution(object):
#     def longestPalindrome(self,s):
#         length=len(s)
#         dp=[[0 for i in range(length)] for i in range(length)]
#         left=0
#         right=0
#         for i in range(length):
#             for j in range(0,i):
#                 dp[j][i]=();
#
#         #print(dp)
#         return ""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp=[[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            for j in range(len(s)):
                if i==j:
                    dp[i][j]=True
        max=1
        res=""
        for i in range(len(s)-1,-1,-1):
            for j in range(i,len(s)):
                # if dp[i][j]:
                #     continue
                if (j-i<=2 or dp[i+1][j-1]) and s[i]==s[j]:
                    dp[i][j]=True
                    if j-i+1>=max:
                        res=s[i:j+1]
                        max=j-i+1
        return res
s=Solution()
b=s.longestPalindrome("abc")
print(b)


#http://www.cnblogs.com/yuzhangcmu/p/4189068.html

