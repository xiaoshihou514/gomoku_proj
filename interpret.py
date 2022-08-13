# $current is a 15x15 matrix
# returns a list of bools [someone_has_won,is_black_winning]

WIN_CONDITION = [1,1,1,1,1]
ENEMY_WIN_CONDITION = [2,2,2,2,2]

def is_at_win_state(current):
    print()
    for some in current:
        print("",some)
    print()
    # horizontal detection
    for i in range(0,15):
        for j in range(0,10):
            if current[i][j:j+5] == WIN_CONDITION:
                return [True,True]
            elif current[i][j:j+5] == ENEMY_WIN_CONDITION:
                return [True,False]
    # vertical detection
    for i in range(0,15):
        col = []
        for j in range(0,15):
            col.append(current[j][i])
        for k in range(0,10):
            if col[k:k+5] == WIN_CONDITION:
                return [True,True]
            elif col[k:k+5] == ENEMY_WIN_CONDITION:
                return [True, False]    
    # diagonal detection
    for i in range(4,15):
        match =[]
        for x in range(0,i+1):
            match.append(current[i-x][x])
        for j in range(0,len(match)-4):
            slice = match[j:j+5]
            if slice == WIN_CONDITION:
                return [True,True]
            elif slice == ENEMY_WIN_CONDITION:
                return [True,False]
    for i in range(4,15):
        match = []
        for x in range(0,i+1):
            match.append(current[14-i-x][14-i+x])
        for j in range(0,len(match)-4):
            slice = match[j:j+5]
            if slice == WIN_CONDITION:
                return [True,True]
            elif slice == ENEMY_WIN_CONDITION:
                return [True,False]
    # diagonal detection rotated
    for i in range(4,15):
        match =[]
        for x in range(0,i+1):
            match.append(current[x][14-i+x])
        for j in range(0,len(match)-4):
            slice = match[j:j+5]
            if slice == WIN_CONDITION:
                return [True,True]
            elif slice == ENEMY_WIN_CONDITION:
                return [True,False]
    for i in range(4,15):
        match =[]
        for x in range(0,i+1):
            match.append(current[14-i+x][x])
        for j in range(0,len(match)-4):
            slice = match[j:j+5]
            if slice == WIN_CONDITION:
                return [True,True]
            elif slice == ENEMY_WIN_CONDITION:
                return [True,False]
    return [False,False]

# Check if the board has sth other than 0, 1 or 2
def board_corrupted(board):
    for row in board:
        for item in row:
            if item != 0 and item != 1 and item != 2:
                return True
    return False