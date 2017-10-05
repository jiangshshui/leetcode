class Solution(object):
    def countAndSay(self, n):
        if n==1:
            return "1"
        preStr=self.countAndSay(n-1)
        length=len(preStr)
        resultStr=""
        count=1
        index=0
        while index<length:
            if index+1==length or preStr[index]!=preStr[index+1]:
                resultStr+=str(count) + str(preStr[index])
                count=1
                index+=1
                continue
            else:
                while index+1<length and preStr[index]==preStr[index+1]:
                    index+=1
                    count+=1
                resultStr += str(count) + str(preStr[index])
                count=1
                index+=1
        return resultStr



s=Solution()
print(s.countAndSay(9))


# def test(preStr):
#     length = len(preStr)
#     resultStr = ""
#     count = 1
#     index = 0
#     while index < length:
#         if index + 1 == length or preStr[index] != preStr[index + 1]:
#             resultStr += str(count) + str(preStr[index])
#             count = 1
#             index += 1
#             continue
#         else:
#             while index + 1 < length and preStr[index] == preStr[index + 1]:
#                 index += 1
#                 count += 1
#             resultStr += str(count) + str(preStr[index])
#             index += 1
#             count=1
#     return resultStr
#
# print(test('111221'))