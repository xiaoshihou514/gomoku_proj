from ast import Param
from threading import Thread
import compute

# I think depth can only be odd
# If it's the last search, it would return an array [score, x, y]
# Else, it would trace recursively to find the best move and return [score, x , y]
# Parent score is used to prune nodes
def search(depth, current):
    tree = []
    for i in range(0,15):
        for j in range(0,15):
            is_upper_bound = j == 0
            is_lower_bound = j == 14
            is_left_bound = i == 0
            is_right_bound = i == 14
            # Check if there's a non empty neighbor and compute score if so
            if not is_upper_bound:
                if current[i][j-1] != 0:    
                    thread = Thread(target=compute.compute_score,args=(current,i,j,tree))
                    thread.start()
                    thread.join()
                    pass
                if not is_left_bound:
                    if current[i-1][j-1] != 0 or current[i-1][j] != 0: 
                        thread = Thread(target=compute.compute_score,args=(current,i,j,tree))
                        thread.start()
                        thread.join()
                        pass
                if not is_right_bound:
                    if current[i+1][j-1] or current[i+1][j] != 0: 
                        thread = Thread(target=compute.compute_score,args=(current,i,j,tree))
                        thread.start()
                        thread.join()    
            if not is_lower_bound:
                if current[i][j+1] != 0:
                    thread = Thread(target=compute.compute_score,args=(current,i,j,tree))
                    thread.start()
                    thread.join()
                if not is_left_bound and current[i-1][j+1]:
                    thread = Thread(target=compute.compute_score,args=(current,i,j,tree))
                    thread.start()
                    thread.join()
                if not is_right_bound and current[i+1][j+1]:
                    thread = Thread(target=compute.compute_score,args=(current,i,j,tree))
                    thread.start()
                    thread.join()     
    if depth == 1:
        max = tree[0]
        for item in range(0,len(tree)):
            if item[0] > max[0]:
                max = item
        return max        
    else:
        score_board = []
        for item in tree:
            context = commit_move(item[0], item[2], current)
            enemy_tree = []
            for i in range(0,15):
                for j in range(0,15):
                    is_upper_bound = j == 0
                    is_lower_bound = j == 14
                    is_left_bound = i == 0
                    is_right_bound = i == 14
                    # Check if there's a non empty neighbor and compute score if so
                    if not is_upper_bound:
                        if current[i][j-1] != 0:    
                            thread = Thread(target=compute.compute_score_rev_core,args=(context,i,j,enemy_tree))
                            thread.start()
                            thread.join()
                            pass
                        if not is_left_bound:
                            if current[i-1][j-1] != 0 or current[i-1][j] != 0: 
                                thread = Thread(target=compute.compute_score_rev_core,args=(context,i,j,enemy_tree))
                                thread.start()
                                thread.join()
                                pass
                        if not is_right_bound:
                            if current[i+1][j-1] or current[i+1][j] != 0: 
                                thread = Thread(target=compute.compute_score_rev_core,args=(context,i,j,enemy_tree))
                                thread.start()
                                thread.join()    
                    if not is_lower_bound:
                        if current[i][j+1] != 0:
                            thread = Thread(target=compute.compute_score_rev_core,args=(context,i,j,enemy_tree))
                            thread.start()
                            thread.join()
                        if not is_left_bound and current[i-1][j+1]:
                            thread = Thread(target=compute.compute_score_rev_core,args=(context,i,j,enemy_tree))
                            thread.start()
                            thread.join()
                        if not is_right_bound and current[i+1][j+1]:
                            thread = Thread(target=compute.compute_score_rev_core,args=(context,i,j,enemy_tree))
                            thread.start()
                            thread.join() 
            max = enemy_tree[0]
            for item in enemy_tree:
                if item[0] > max[0]:
                    max = item   
            new_depth = depth - 2
            context = commit_move(max[1], max[2], context)
            next_best_move = search(new_depth, context)         
            score_board.append(item[1],item[2],item[0]-max[0]+next_best_move[0]) 
        for item in score_board:
            if item[0] > max[0]:
                max = item   
        return max
             
def commit_move(x, y, current):
    current[x][y] = 1
    return current                    