'''
第一种算法：
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping={
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        length=len(digits)
        if length==0:
            return []
        if length==1:
            return  list(mapping[digits[0]])
        else:
            preffix=self.letterCombinations(digits[:-1])
            suffix=self.letterCombinations(digits[-1])
            return [s+t for s in preffix for t in suffix]

'''


'''
第二种算法  尚不理解
class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if '' == digits: return []
        kvmaps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return reduce(lambda acc, digit: [x + y for x in acc for y in kvmaps[digit]], digits, [''])
        
'''
class Solution(object):
    def letterCombinations(self, digits):
        mapping={
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        length=len(digits)
        if length==0:
            return []
        ret=['']
        for x in digits:
            temp=[]
            for y in ret:
                for t in mapping[x]:
                    temp.append(y+t)
            ret=temp
        return ret



s=Solution()
result=s.letterCombinations("23")
print(result)