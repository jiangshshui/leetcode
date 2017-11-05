class Solution(object):
    def exist(self, board, word):
        #visited=[[False for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    #visited[i][j]=True
                    if(self.traverse(board,word,i,j)):
                        return True
                    #visited[i][j]=False
        return False

    def traverse(self, board, word, i, j):
        if len(word) == 0:  # all the characters are checked
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = '#'
        #visited[i][j] = True  # avoid visit agian
        # check whether can find "word" along one direction
        res = self.traverse(board, word[1:], i + 1, j) or self.traverse(board, word[1:], i - 1, j) \
              or self.traverse(board, word[1:], i, j + 1) or self.traverse(board, word[1:], i, j - 1)
        board[i][j]=tmp
        return res

    # def traverse(self,board,word,visited,i,j):
    #     if len(word)==0:
    #         return True
    #     if(i-1>=0 and not visited[i-1][j] and board[i-1][j]==word[0]):
    #         visited[i-1][j]=True
    #         return self.traverse(board,word[1:],visited,i-1,j)
    #     elif (i+1<len(board) and not visited[i+1][j] and board[i+1][j]==word[0]):
    #         visited[i+1][j]=True
    #         return self.traverse(board,word[1:],visited,i+1,j)
    #     elif (j-1>=0 and not visited[i][j-1] and board[i][j-1]==word[0]):
    #         visited[i][j-1]=True
    #         return self.traverse(board,word[1:],visited,i,j-1)
    #     elif (j+1<len(board[0]) and not visited[i][j+1] and board[i][j+1] == word[0]):
    #         visited[i][j+1] = True
    #         return self.traverse(board, word[1:], visited, i, j+1)
    #     else:
    #         visited[i][j]=False
    #         return False


s=Solution()
# res=s.exist([
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ],"ABCCED")
# res=s.exist([["b"],["a"],["b"]],
# "bbabab")
res=s.exist([["C","A","A"],["A","A","A"],["B","C","D"]],"AAB")
print(res)