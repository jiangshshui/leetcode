# class Solution(object):
#     def removeKdigits(self, num, k):
#         stack=[]
#         if k==0:
#             return num
#         i=0
#         stack.append(int(num[0]))
#         index=1
#         while i<k and len(stack)!=0 and index<len(num):
#             if stack[-1]<=int(num[index]):
#                 stack.append(int(num[index]))
#                 index+=1
#             else:
#                 stack.pop()
#                 i+=1
#                 if(len(stack)==0):
#                     stack.append(int(num[index]))
#                     index+=1
#         while i<k:
#             stack.pop()
#             i+=1
#
#         while index<len(num):
#             stack.append(int(num[index]))
#             index+=1
#         res=""
#         for item in stack:
#             res+=str(item)
#
#         if res.startswith("0"):
#             res=res.lstrip('0')
#         if len(res) == 0:
#             return "0"
#         return res


class Solution(object):
    def removeKdigits(self, num, k):
        stack=[]
        stack.append(num[0])
        for i in range(1,len(num)):
            while stack and k and stack[-1]>num[i]:
                stack.pop()
                k-=1
            stack.append(num[i])

        if stack:
            offset=-k if k>0 else None
            ans="".join(stack[:offset]).lstrip('0')
        return ans if ans else "0"
s=Solution()
print(s.removeKdigits("5337",2))
