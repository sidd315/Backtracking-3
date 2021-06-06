class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        self.m,self.n = len(board), len(board[0])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                    if self.backtrack(board, word, i, j, 0):
                        return True
        return False
    
    
    def backtrack(self, board, word, i, j, index):
        #base
        if index==len(word):
            return True
        
        if i<0 or j< 0 or i==self.m or j==self.n or board[i][j]=="#":
            # print(i,j)
            return False
        #logic
        dirs = ((1,0),(0,1),(-1,0),(0,-1))
        if word[index] == board[i][j]:
            temp = board[i][j]
            board[i][j] = '#'
            for dir in dirs:
                r = i + dir[0]
                c = j + dir[1]
                if self.backtrack(board, word, r,c,index+1):
                    
                    return True
            
            board[i][j] = temp
        return False
        
        
        
