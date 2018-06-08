class Solution:

    def after_back(self,str):
        stack=[]
        for ch in str:
            if ch!='#':
                stack.append(ch)
            else:
                if len(stack)!=0:
                    stack.pop()
        return "".join(stack)

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        if self.after_back(S)==self.after_back(T):
            return True
        return False




s=Solution()
print(s.backspaceCompare("ab#cd#","ad#c"))