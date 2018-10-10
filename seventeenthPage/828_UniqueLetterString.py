# class Solution:
#     def findAllSubString(self,S):
#         subStrings=[]
#         for i in range(1,len(S)+1):
#             for j in range(len(S)+1-i):
#                 subStrings.append(S[j:i+j])
#         return subStrings
#     def calculateUnique(self,S):
#         m={}
#         for ch in S:
#             if ch not in m:
#                 m[ch]=1
#             else:
#                 m[ch]+=1
#         count=0
#         for value in m.values():
#             if value==1:
#                 count+=1
#         return count
#     def uniqueLetterString(self, S):
#         """
#         :type S: str
#         :rtype: int
#         """
#         res=0
#         subStrings=self.findAllSubString(S)
#         for sub in subStrings:
#             res+=self.calculateUnique(sub)
#         return res

import string

class Solution:
    def uniqueLetterString(self, S):
        """
        :type S: str
        :rtype: int
        """
        index={c:[-1,-1] for c in string.ascii_uppercase}
        '''
        #index 中存的是c 出现的前两次index
        0123456789
        ***A**A**A
        当扫描到第一个A时   index=[-1,-1]
        当扫描到第二个A时   index=[-1,3]
        当扫描到第三个A时   index=[3,6]
        
        '''

        res=0
        for i,c in enumerate(S):
            k,j=index[c]
            res+=(i-j)*(j-k)
            index[c]=[j,i]

        for c in index:
            k,j=index[c]
            res+=(len(S)-j)*(j-k)

        return res%(10**9+7)

if __name__=="__main__":
    s=Solution()
    print(s.uniqueLetterString("ABA"))
    print(s.uniqueLetterString("ABC"))

