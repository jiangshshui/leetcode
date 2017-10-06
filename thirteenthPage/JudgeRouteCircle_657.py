'''
第一种算法:(时间太慢)
class Solution(object):
    def judgeCircle(self, moves):
        directionAdd=['L','U']
        directionMiu=['R','D']
        countHron=0
        countVer=0
        for ch in moves:
            if ch in directionAdd :
                if ch =='L':
                    countHron+=1
                else:
                    countVer +=1
            elif ch in directionMiu:
                if ch=='R':
                    countHron-=1
                else:
                    countVer-=1
        return True if countVer==0 and countHron==0 else False
'''
class Solution(object):
    def judgeCircle(self, moves):
        if len(moves)%2!=0:
            return False
        return moves.count('L')==moves.count('R') and moves.count('U')==moves.count("D")


s=Solution()
print(s.judgeCircle("UD"))
