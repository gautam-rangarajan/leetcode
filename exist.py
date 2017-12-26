class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        
        for i in range(rows):
            for j in range(cols):
                if(board[i][j] == word[0]):
                    temp = board[i][j]
                    board[i][j] = -1
                    #print word
                    found = self.bfs(i, j, board, word[1:])
                    board[i][j] = temp
                    if(found):
                        return True
        return False
                    
                    
    def bfs(self, i, j, board, word):
        #print(i, j, board, word, len(word))
        rows = len(board)
        cols = len(board[0])
        if len(word) == 0:
            #print "------------------------------------------"
            return 1

        found = 0

        if(i > 0):
            if(board[i-1][j] == word[0]):
                temp = board[i-1][j]
                board[i-1][j] = -1
                found = self.bfs(i-1, j, board, word[1:])
                board[i-1][j] = temp

        if(found):
            return 1

        if(i < rows-1):
            if(board[i+1][j] == word[0]):
                temp = board[i+1][j]
                board[i+1][j] = -1
                found = self.bfs(i+1, j, board, word[1:])
                board[i+1][j] = temp

        if(found):
            return 1
        
        if(j > 0):
            if(board[i][j-1] == word[0]):
                temp = board[i][j-1]
                board[i][j-1] = -1
                found = self.bfs(i, j-1, board, word[1:])
                board[i][j-1] = temp

        if(found):
            return 1

        if(j < cols-1):
            if(board[i][j+1] == word[0]):
                temp = board[i][j+1]
                board[i][j+1] = -1
                found = self.bfs(i, j+1, board, word[1:])
                board[i][j+1] = temp

        if(found):
            return 1

        return 0

        