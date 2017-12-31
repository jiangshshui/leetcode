class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
    def __str__(self):
        return str(self.x)+","+str(self.y)
from collections import defaultdict
# class Solution(object):
#     def maxPoints(self, points):
#         res=0
#         for i in range(len(points)):
#             d = defaultdict(int)
#             vertical = 1
#             same=0
#             local=1
#             slope=0
#             for j in range(i+1,len(points)):
#                 if points[i].x==points[j].x:#x轴相同
#                     if points[i].y==points[j].y:
#                         same+=1
#                     else:
#                         vertical+=1
#                 else:
#                     slope=(points[j].y-points[i].y)/(points[j].x-points[i].x)
#                     d[slope]=d[slope]+2 if d[slope]==0 else d[slope]+1
#                     local=max(local,d[slope])
#             local=max(local+same,vertical+same)
#             res=max(res,local)
#             print(d)
#         return res


class Solution(object):

    def gcd(self,x,y):
        while(y):
            x,y=y,x%y
        return x
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        res=0
        for i in range(len(points)):
            same_point=0
            d=defaultdict(int)
            vertical_point=1
            local=1
            for j in range(i+1,len(points)):
                if points[i].x==points[j].x:
                    if points[i].y==points[j].y:
                        same_point+=1
                    else:
                        vertical_point+=1
                else:
                    #print(points[i],points[j])
                    y_span=points[i].y-points[j].y
                    x_span=points[i].x-points[j].x
                    div=self.gcd(y_span,x_span)
                    if d[(y_span//div,x_span//div)]==0:
                        d[(y_span//div,x_span//div)]+=2
                    else:
                        d[(y_span // div, x_span // div)] += 1
                    local=max(local,d[(y_span//div,x_span//div)])
            local=max(local+same_point,vertical_point+same_point)
            res=max(res,local)
        return res







def lists2points(lists):
    res=[]
    for item in lists:
        res.append(Point(item[0],item[1]))
    return res


s=Solution()
print(s.maxPoints(lists2points([[84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]])))

# def gcd(x, y):
#     # if x<y:
#     #     x,y=y,x
#     while (y):
#         temp=x
#         # x, y = y, x % y
#         x=y
#         y=temp%y
#     return x
#
# print(gcd(0,-1))


# import matplotlib.pyplot as plt
# X=[]
# Y=[]
# for item in [[84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]]:
#     X.append(item[0])
#     Y.append(item[1])
# plt.scatter(X,Y)
# plt.show()







