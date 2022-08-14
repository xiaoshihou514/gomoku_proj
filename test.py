import interpret, search, chessboard
context = [[0,0,0,0,2,0,0,0,1,1,1,1,0,0,2],
           [0,0,0,2,0,0,0,0,0,0,0,1,0,0,1],
           [0,0,2,0,0,0,0,0,0,0,0,0,1,0,1],
           [0,2,0,0,0,0,0,0,0,0,0,0,1,2,1],
           [0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
           [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,1,0,2,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
           [1,0,0,0,0,2,2,2,2,2,0,0,0,0,0],
           [0,2,0,0,0,0,0,0,0,0,0,0,2,0,0],
           [0,0,2,0,0,0,0,0,0,0,0,2,0,0,0],
           [0,0,0,2,0,0,0,0,0,0,2,0,0,0,0],
           [0,0,0,0,2,0,0,0,0,2,0,0,0,0,0]]
# 1 is black piece, 2 is white piece
print("",interpret.is_at_win_state(context))

print("", search.search(3, chessboard.store_chess))