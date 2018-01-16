class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g=sorted(g)
        s=sorted(s)
        total_contents=0
        i=0
        j=0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                i+=1
                j+=1
                total_contents+=1
            else:
                j+=1
        return total_contents





if __name__=="__main__":
    s = Solution()
    print(s.findContentChildren([1, 2, 3], [1, 3]))
