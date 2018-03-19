import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        numStack=[]
        operator=['+','-','*','/']
        for ch in tokens:
            if ch in operator:
                num1=numStack.pop()
                num2=numStack.pop()
                if ch =="+":
                    numStack.append(num1+num2)
                elif ch=="-":
                    numStack.append(num2-num1)
                elif ch=="*":
                    numStack.append(num1*num2)
                else:
                    if num2/num1<0:
                        numStack.append(math.ceil(num2/num1))
                    else:
                        numStack.append(num2//num1)
            else:
                numStack.append(int(ch))
        return numStack[0]


s=Solution()
print(s.evalRPN(["2", "1", "+", "3", "*"]))
print(s.evalRPN( ["4", "13", "5", "/", "+"]))
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))