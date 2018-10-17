
# class Solution:
#     def pushDominoes(self, dominoes):
#         """
#         :type dominoes: str
#         :rtype: str
#         """
#         symbols=[(i,x) for i,x in enumerate(dominoes) if x!="."]
#         symbols=[(-1,'L')]+symbols+[(len(dominoes),'R')]
#         ans=list(dominoes)
#         def cmp(a,b):
#             if a==b:
#                 return 0
#             elif a<b:
#                 return -1
#             else:
#                 return 1
#         for (i,x),(j,y) in zip(symbols,symbols[1:]):
#             if x==y:
#                 for k in range(i+1,j):
#                     ans[k]=x
#             elif x>y:
#                 for k in range(i+1,j):
#                     ans[k]=".LR"[cmp(k-i,j-k)]
#         return "".join(ans)


class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        N=len(dominoes)
        force=[0]*N
        f=0

        for i in range(N):
            if dominoes[i]=="R":
                f=N
            elif dominoes[i]=="L":
                f=0
            else:
                f=max(f-1,0)
            force[i]+=f

        for i in range(N-1,-1,-1):
            if dominoes[i]=="L":
                f=N
            elif dominoes[i]=="R":
                f=0
            else:
                f=max(f-1,0)
            force[i]-=f

        return "".join(["." if f==0 else "R" if f>0 else "L" for f in force])





if __name__=="__main__":
    s=Solution()
    print(s.pushDominoes(".L.R...LR..L.."))