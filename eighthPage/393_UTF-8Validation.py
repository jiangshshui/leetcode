# class Solution:
#     def validUtf8(self, data):
#         """
#         :type data: List[int]
#         :rtype: bool
#         """
#         # 240-247 128-191
#         # 224 -239
#         # 192-223
#         # 127
#         i=0
#         while i<len(data):
#             if data[i]>=240 and data[i]<=247:
#                 j=i+1
#                 while j<=min(i+3,len(data)-1) and data[j]>=128 and data[j]<=191:
#                     j+=1
#                 if j-i==4:
#                     i=j
#                 else:
#                     return False
#
#             elif data[i]>=224 and data[i]<=239:
#                 j=i+1
#                 while j<=min(i+2,len(data)-1) and data[j]>=128 and data[j]<=191:
#                     j+=1
#                 if j-i==3:
#                     i=j
#                 else:
#                     return False
#
#             elif data[i]>=192 and data[i]<=223:
#                 j=i+1
#                 while j<=min(i+1,len(data)-1) and data[j]>=128 and data[j]<=191:
#                     j+=1
#                 if j-i==2:
#                     i=j
#                 else:
#                     return False
#
#             elif data[i]>=0 and data[i]<=127:
#                 i+=1
#             else:
#                 return False
#         return True


class Solution:
    def validUtf8(self, data):
        n = 0

        for i in reversed(range(len(data))):
            byte = '{:08b}'.format(data[i])

            if byte.startswith('0'):
                if n > 0:
                    return False
            elif byte.startswith('10'):
                n += 1
                if n == 4:
                    return False
            elif byte.startswith('1' + '1' * n + '0'):
                n = 0
            else:
                return False

        return n == 0


if __name__=="__main__":
    s=Solution()
    # print(s.validUtf8([197, 130, 1]))
    # print(s.validUtf8([235, 140, 4]))
    print(s.validUtf8([230,136,145]))