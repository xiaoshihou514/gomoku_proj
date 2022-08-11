# $current is a 15x15 matrix
# returns a list of bools [someone_has_won,is_black_winning]
from nis import match


def has_win_state(current):
    # horizontal detection
    for i in range(0,15):
        for j in range(0,10):
            if current[i][j:j+5] == [1,1,1,1,1]:
                return [True,True]
            elif current[i][j:j+5] == [2,2,2,2,2]:
                return [True,False]
    # vertical detection
    for i in range(0,10):
        for j in range(0,15):
            if current[i:i+5][j] == [1,1,1,1,1]:
                return [True,True]
            elif current[i:i+5][j] == [2,2,2,2,2]:
                return [True,False]
    # diagnal detection
    for i in range(4,11):
        match = []
        for x in range(0,i+1):
            # !TODO
            pass 