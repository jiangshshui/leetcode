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



class Solution(object):
    def longestPalindrome(self,s):
        length=len(s)
        dp=[[0 for i in range(length)] for i in range(length)]
        left=0
        right=0
        for i in range(length):
            for j in range(0,i):
                dp[j][i]=();

        #print(dp)


        return ""


s=Solution()
b=s.longestPalindrome("aba")
print(b)


