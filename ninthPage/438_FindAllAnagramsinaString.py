'''
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
'''
class Solution:

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res=[]
        if s is None or p is None or len(s)<len(p):
            return res
        m = {}
        for ch in p:
            if ch not in m:
                m[ch]=1
            else:
                m[ch]+=1
        begin=end=0
        counter=len(m)
        while end<len(s):
            if s[end] in m:
                m[s[end]]-=1
                if m[s[end]]==0:
                    counter-=1
            end+=1
            while counter==0:
                if end-begin==len(p):
                    res.append(begin)
                if s[begin] in m:
                    m[s[begin]]+=1
                    if m[s[begin]]>0:
                        counter+=1
                begin+=1
        return res





s=Solution()
print(s.findAnagrams("cbaebabacd","abc"))