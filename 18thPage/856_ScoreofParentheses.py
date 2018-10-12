class Solution:
    def next_position(self,s):
        stack=[]
        for index,ch in enumerate(s):
            if ch == "(":
                stack.append(ch)
            else:
                stack.pop()
                if not stack:
                    return index
        return len(s)


    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        if S=="()":
            return 1
        next=self.next_position(S)
        if next==len(S)-1:
            return 2*self.scoreOfParentheses(S[1:-1])
        else:
            return self.scoreOfParentheses(S[:next+1])+self.scoreOfParentheses(S[next+1:])






if __name__=="__main__":
    s=Solution()
    print(s.scoreOfParentheses("(()(()))"))