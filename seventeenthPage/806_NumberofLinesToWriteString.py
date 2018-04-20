class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        lines=1
        now=0
        for i in range(len(S)):
            if now+widths[ord(S[i])-ord('a')]>100:
                lines+=1
                now=widths[ord(S[i])-ord('a')]
            else:
                now+=widths[ord(S[i])-ord('a')]
        return [lines,now]
s=Solution()
print(s.numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                      "abcdefghijklmnopqrstuvwxyz"))

print(s.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                      "bbbcccdddaaa"))