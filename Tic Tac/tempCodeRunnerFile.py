
        pattern = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    
        for x in pattern:
            if all(y in playerPosition[currPlayer] for y in x) :
                return True
            return False
    
def resultIsDraw(playerPosition):
        if len(playerPosition['X']) +  len(playerPosition['O']) == 9 :
            return True
        return False    

def currGame(currPlayer) :
    value = [' ' for x in range (9)]
    playerPosition = {'X':[], 'O':[]}
            