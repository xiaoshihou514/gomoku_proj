# defines the opening move logic
def opening_move(current):
    # First move
    sanity_check = check_state(current)
    if sanity_check[0] or sanity_check[1]:
        return [7,7]
    # If not first move
    else:
        # !TODO
        exit(-1)

# 
def check_state(current):
    is_null = True
    center_empty = False
    opponent_count = 0
    for i in range(0,15):
        for j in range(0,15):
            if current[i][j] != 0:
                is_null = False
                # Is enemy piece
                if current[i][j] == 2:
                    opponent_count += 1
    if opponent_count == 1 and current[7][7] == 0:
         center_empty == True
    return [is_null, center_empty]            
                