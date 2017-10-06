class Solution(object):
    def calPoints(self, ops):
        total=0
        stack=[]
        for op in ops:
            if op=="C":
                stack.pop()
            elif op=="D":
                top=stack[-1]
                stack.append(top*2)
            elif op=="+":
                top,sectop=stack[-1],stack[-2]
                stack.append(top+sectop)
            else:
                stack.append(int(op))
        return sum(stack)

s=Solution()
print(s.calPoints(["5","-2","4","C","D","9","+","+"]))
