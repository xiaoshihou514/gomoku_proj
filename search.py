from threading import Thread
import compute

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