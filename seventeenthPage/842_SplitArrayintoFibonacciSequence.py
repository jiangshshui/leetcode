class Solution:
    def splitIntoFibonacci(self, S):
        limit=2**31-1
        if len(S)<=2:
            return []
        for i in range(1,len(S)//2+1):
            for k in range(1,len(S)-i):
                nums = []
                j=0
                if len(S[0:i])>1 and S[0]=='0':
                    break
                if int(S[0:i])>limit:
                    break
                nums.append(int(S[0:i]))
                if int((S[i:i+k]))>limit:
                    break
                if len(S[i:i+k])>1 and S[i]=='0':
                    break
                nums.append(int(S[i:i+k]))
                j=i+k
                while j<len(S):
                    res=str(nums[-2]+nums[-1])
                    if int(res)>limit:
                        break
                    if j+len(res)>len(S):
                        break
                    if res==S[j:j+len(res)]:
                        j+=len(res)
                        nums.append(int(res))
                    else:
                        break
                if j>=len(S):
                    return nums
        return []

# class Solution:
#     def splitIntoFibonacci(self, S):
#         """
#         :type S: str
#         :rtype: List[int]
#         """
#         limit=2**31 - 1
#         for i in range(1,len(S)):
#             if S[0]=="0" and i!=1:
#                 break
#             for j in range(i+1,len(S)):
#                 if S[i]=="0" and j!=i+1:
#                     break
#                 pre=int(S[:i])
#                 cur=int(S[i:j])
#                 ans=[pre,cur]
#                 k=j
#                 while k<len(S):
#                     cur,pre=pre+cur,cur
#                     if cur<=limit and str(cur)==S[k:k+len(str(cur))]:
#                         ans.append(cur)
#                         k=k+len(str(cur))
#                     else:
#                         break
#                 if k==len(S):
#                     return ans
#         return []
s=Solution()

# print(s.splitIntoFibonacci("123456579"))
# print(s.splitIntoFibonacci("11235813"))
# print(s.splitIntoFibonacci("112358130"))
# print(s.splitIntoFibonacci("0123"))
# print(s.splitIntoFibonacci("1101111"))
# print(s.splitIntoFibonacci("00000"))
# print(s.splitIntoFibonacci("0224"))
# print(s.splitIntoFibonacci("17522"))
# print(s.splitIntoFibonacci("0123"))
print(s.splitIntoFibonacci("1023"))

