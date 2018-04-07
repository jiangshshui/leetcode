class Solution:
    def __init__(self):
        self.visited=None
        self.res=[]
        self.step=[(-1,0),(1,0),(0,-1),(0,1)]
        self.m=0
        self.n=0
    def dfs(self,x,y,board,temp):
        try:
            for i,j in self.step:
                if x+i>=0 and x+i<self.m and y+j>=0 and y+j<self.n and \
                        not self.visited[x+i][y+j] and board[x+i][y+j]=='O':
                    temp.append((x+i,y+j))
                    self.visited[x+i][y+j]=True
                    self.dfs(x+i,y+j,board,temp)
        except Exception as err:
            print((x+i,y+j))
            print(err)

    def solve(self, board):
        self.m=len(board)#行
        if self.m==0:
            return
        self.n=len(board[0])#列
        self.visited=[[False for _ in range(self.n)] for _ in range(self.m)]
        self.res=[]
        for i in range(self.m):
            for j in range(self.n):
                if (i==0 or i==self.m-1 or j==0 or j==self.n-1) and board[i][j]=='O':
                    temp=[]
                    temp.append((i,j))
                    self.visited[i][j]=True
                    self.dfs(i,j,board,temp)
                    self.res.append(temp)
        for i in range(self.m):
            for j in range(self.n):
                board[i][j]='X'

        for item in self.res:
            for k in range(len(item)):
                board[item[k][0]][item[k][1]]='O'
        return board
s=Solution()
print(s.solve([["O","O"],
               ["O","O"]]))

# print(s.solve([["X","X","X","X"],
#                ["X","O","O","X"],
#                ["X","X","O","X"],
#                ["X","O","X","X"]]))