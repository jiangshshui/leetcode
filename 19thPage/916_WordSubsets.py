class Solution:
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        def count(word):
            ans=[0]*26
            for letter in word:
                ans[ord(letter)-ord('a')]+=1
            return ans

        bmax=[0]*26
        for b in B:
            for i,w in enumerate(count(b)):
                bmax[i]=max(bmax[i],w)

        ans=[]
        for a in A:
            if all(x>=y for x,y in zip(count(a),bmax)):
                ans.append(a)
        return ans




if __name__=="__main__":
    s=Solution()
    print(s.wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]))