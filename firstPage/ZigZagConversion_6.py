# class Solution(object):
#     def convert(self, s, numRows):
#         """
#         :type s: str
#         :type numRows: int
#         :rtype: str
#         """
#         if numRows==1:
#             return s
#         res=["" for i in range(numRows)]
#         j=0
#         isAdd=True
#         for i in range(len(s)):
#             if isAdd:
#                 #res[j].append(s[i])
#                 res[j]+=s[i]
#                 j+=1
#             if not isAdd:
#                 j-=1
#                 #res[j].append(s[i])
#                 res[j]+=s[i]
#             if j==numRows:
#                 isAdd=False
#                 j-=1
#             elif j==0:
#                 isAdd=True
#                 j+=1
#         result=""
#         # for i in res:
#         #     temp="".join(i)
#         #     result+=temp
#         for i in res:
#             result+=i
#         return result


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1
        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step
        return ''.join(L)

s=Solution()
print(s.convert("ABCdef",3))