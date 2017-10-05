class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping={'{':'}','[':']','(':')'}
        stack=[]
        for ch in s:
            if ch in mapping.keys():
                stack.append(ch)
            elif ch in mapping.values():
                if len(stack)==0 or ch!=mapping[stack.pop()]:
                    return False
                continue
            else:
                return False
        return True if len(stack)==0 else False

s=Solution()
print(s.isValid("["))
