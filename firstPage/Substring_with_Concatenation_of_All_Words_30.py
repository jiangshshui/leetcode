

# from collections import defaultdict
# class Solution(object):
#     def findSubstring(self, s, words):
#         """
#         :type s: str
#         :type words: List[str]
#         :rtype: List[int]
#         """
#         res=[]
#         if len(s)==0 and len(words)==0:
#             return res
#         n=len(words)
#         m=len(words[0])
#         m1=defaultdict(int)
#         for word in words:
#             m1[word]+=1
#
#         for i in range(0,len(s)-n*m+1):
#             m2=defaultdict(int)
#             for j in range(0,n):
#                 t=s[i+j*m:i+(j+1)*m]
#                 if m1[t]==0:
#                     break
#                 m2[t]+=1
#                 if m2[t]>m1[t]:
#                     break
#                 if j+1==n:
#                     res.append(i)
#         return res


from collections import defaultdict
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        #d=defaultdict(int)
        res = []
        if len(s)==0 and len(words)==0:
            return res
        n=len(s)
        cnt=len(words)
        wordLen=len(words[0])
        mword=defaultdict(int)
        for word in words:
            mword[word]+=1

        for i in range(0,wordLen):
            left=i
            count=0
            mtarget=defaultdict(int)
            for j in range(i,n-wordLen+1,wordLen):
                t=s[j:j+wordLen]
                if mword[t]:
                    mtarget[t]+=1
                    if mtarget[t]<=mword[t]:
                        count+=1
                    else:
                        while mtarget[t]>mword[t]:
                            t1=s[left:left+wordLen]
                            mtarget[t1]-=1
                            if mtarget[t1]<mword[t1]:
                                count-=1
                            left+=wordLen
                    if count==cnt:
                        res.append(left)
                        mtarget[s[left:left+wordLen]]-=1
                        count-=1
                        left+=wordLen
                else:
                    mtarget.clear()
                    count=0
                    left=j+wordLen
        return res
s=Solution()
print(s.findSubstring("barfooabcthefoobarbarfooabcman",["foo", "bar","abc"]))