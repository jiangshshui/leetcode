class Solution(object):
    def isValidSudoku(self,board):
        if not board:
            return False
        rowcheck=[[0 for i in range(9)] for j in range(9)]
        colcheck = [[0 for i in range(9)] for j in range(9)]
        boxcheck = [[0 for i in range(9)] for j in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!='.':
                    num=int(board[i][j])-1
                    k=i//3*3+j//3
                    if rowcheck[i][num] or colcheck[j][num] or boxcheck[k][num]:
                        return False
                    rowcheck[i][num]=colcheck[j][num]=boxcheck[k][num]=1
        return True


# class Solution(object):
#     def isValidSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: bool
#         """
#         if not board: return False
#         m, n = len(board), len(board[0])
#         check_row = [[0 for i in range(9)] for j in range(9)]  # three 2d array to check each row, col and sub box
#         check_col = [[0 for i in range(9)] for j in range(9)]  # three 2d array to check each row, col and sub box
#         check_box = [[0 for i in range(9)] for j in range(9)]  # three 2d array to check each row, col and sub box
#         for i in range(m):
#             for j in range(n):
#                 if board[i][j] != '.':
#                     num = int(board[i][j]) - 1  # need -1 becasue the index of array is 0~8
#                     k = i // 3 * 3 + j // 3
#                     # because if previously the same number of same row,col or box have exist, it is false
#                     if check_row[i][num] or check_col[j][num] or check_box[k][num]:
#                         return False
#                     # assign value to all the checking 2d arrayes
#                     check_row[i][num] = check_col[j][num] = check_box[k][num] = 1
#         return True
#
#
# boards=[
#     [5,3,0,0,7,0,0,0,0],
#     [6,0,0,1,9,5,0,0,0],
#     [0,9,8,0,0,0,0,6,0],
#     [8,0,0,0,6,0,0,0,3],
#     [4,0,0,8,0,3,0,0,1],
#     [7,0,0,0,2,0,0,0,6],
#     [0,6,0,0,0,0,2,8,0],
#     [0,0,0,4,1,9,0,0,5],
#     [0,0,0,0,8,0,0,7,9]
# ]
#
# s=Solution()
# print(s.isValidSudoku(boards))