# class Solution(object):
#     def generate_str(self,n):
#         if n==1:
#             return [0]
#         str=[]
#         for ch in self.generate_str(n-1):
#             if ch==0:
#                 str.extend([0,1])
#             else:
#                 str.extend([1,0])
#         return str
#     def kthGrammar(self, N, K):
#         """
#         :type N: int
#         :type K: int
#         :rtype: int
#         """
#         str=self.generate_str(N)
#         #print(str)
#         return str[K-1]


class Solution(object):
    def kthGrammar(self, N, K):
        # s=[0]
        # for i in range(N):
        #     temp=[]
        #     for num in s:
        #         if num==0:
        #             temp.extend([0,1])
        #         else:
        #             temp.extend([1,0])
        #     s,temp=temp,s
        # return s[K-1]
        if N==1:
            return 0
        if K%2==1:#左节点
            if self.kthGrammar(N-1,K//2)==0:
                return 0
            else:
                return 1
        else:
            if self.kthGrammar(N-1,K//2)==1:
                return 0
            else:
                return 1

s=Solution()
print(s.kthGrammar(2,1))



'''
0
01
0110
01101001
0110100110010110
0110100110010110  1001 0110 0110 1001
'''