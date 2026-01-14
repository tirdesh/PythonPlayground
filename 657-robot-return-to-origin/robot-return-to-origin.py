class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U')==moves.count("D") and moves.count('L')==moves.count("R") 
        xy = [0,0]
        map = {'U':[1,0],'D':[-1,0],'R':[0,1],'L':[0,-1]}
        for i in moves:
            xy=[map[i][0]+xy[0],map[i][1]+xy[1]]
        return True if xy==[0,0] else False