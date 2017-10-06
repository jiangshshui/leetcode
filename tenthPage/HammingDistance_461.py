'''
第一种算法
# class Solution(object):
#     def hammingDistance(self, x, y):
#         strx=self.int2binarystr(x)
#         stry = self.int2binarystr(y)
#         lengthx=len(strx)
#         lengthy=len(stry)
#         i,j=lengthx-1,lengthy-1
#         count=0
#         while i>=0 and j>=0:
#             if strx[i]!=stry[j]:
#                 count+=1
#             i-=1
#             j-=1
#         while i>=0:
#             if strx[i]!='0':
#                 count+=1
#             i-=1
#         while j>=0:
#             if stry[j]!='0':
#                 count+=1
#             j-=1
#         return count
#     def int2binarystr(self,x):
#         res=""
#         while x!=0:
#             res+=str(x%2)
#             x//=2
#         res=reversed(res)
#         return "".join(res)
'''


'''
第二种算法
class Solution(object):
    def hammingDistance(self, x, y):
        # strx=x.to_bytes(31,'big')
        # stry=x.to_bytes(31,'big')
        # return strx^stry
        return bin(x^y).count('1')
        
'''

class Solution(object):
    def hammingDistance(self, x, y):
        count=0
        while x or y:
            xrightmost=x&1
            yrightmost=y&1
            count+=xrightmost^yrightmost
            x>>=1
            y>>=1
        return count
s=Solution()
res=s.hammingDistance(1,4)
print(res)

