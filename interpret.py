# $current is a 15x15 matrix
# returns a list of bools [someone_has_won,is_black_winning]

import re


WIN_CONDITION = [1,1,1,1,1]
ENEMY_WIN_CONDITION = [2,2,2,2,2]

def is_at_win_state(current):
    # horizontal detection
    for i in range(0,15):
        for j in range(0,10):
            if current[i][j:j+5] == WIN_CONDITION:
                return [True,True]
            elif current[i][j:j+5] == ENEMY_WIN_CONDITION:
                return [True,False]
    # vertical detection
    for i in range(0,10):
        for j in range(0,15):
            if current[i:i+5][j] == WIN_CONDITION:
                return [True,True]
            elif current[i:i+5][j] == ENEMY_WIN_CONDITION:
                return [True,False]
    # diagonal detection
    for i in range(4,11):
        match =[]
        for x in range(0,i+1):
            match.append(current[i-x][i+x])
        for j in range(0,len(match)-5):
            slice = match[j:j+5]
            if slice == WIN_CONDITION:
                return [True,True]
            elif slice == ENEMY_WIN_CONDITION:
                return [True,False]
    for i in range(10,3):
        match = []
        for x in range(0,14-i):
            match.append(current[i-x][i+x])
        for j in range(0,len(match)-5):
            slice = match[j:j+5]
            if slice == WIN_CONDITION:
                return [True,True]
            elif slice == ENEMY_WIN_CONDITION:
                return [True,False]
    for i in range(10,3):
        match = []
        for x in range(0,14-i):
            match.append(current[i+x][i+x])
        for j in range(0,len(match)-5):
            slice = match[j:j+5]
            if slice == WIN_CONDITION:
                return [True,True]
            elif slice == ENEMY_WIN_CONDITION:
                return [True,False]
    for i in range(4,11):
        match =[]
        for x in range(0,i+1):
            match.append(current[i-x][i-x])
        for j in range(0,len(match)-5):
            slice = match[j:j+5]
            if slice == WIN_CONDITION:
                return [True,True]
            elif slice == ENEMY_WIN_CONDITION:
                return [True,False]
    return [False,False]