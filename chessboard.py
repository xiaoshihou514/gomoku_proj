import tkinter as tk
from tkinter import *

PIECE_SIZE = 10
piece_color = "black"

'''Store the location that the pieces have been put'''
axis_black = []
axis_white = []

person_flag = 1


#root window as chess board
root_window = tk.Tk()
root_window.title("Gomoku Game by Kevin Ye & Sihan Chen")
root_window.geometry("995x660")
root_window.resizable(0,0)
#TODO Please change the path of ico to your path after you clone the repo
root_window.iconbitmap('./GomokuIcon.ico')


#chess info
frames = tk.Canvas(root_window, width=220, height=70)
frames.grid(row = 0, column = 1)
frames.create_oval(110 - PIECE_SIZE, 25 - PIECE_SIZE, 110 + PIECE_SIZE, 25 + PIECE_SIZE, fill = piece_color, tags = ("show_pieces"))
var = tk.StringVar()
var.set("Your turn")
person_chess = tk.Label(root_window, textvariable = var, width = 20, anchor = tk.CENTER, font = ("Times New Roman", 15) )
person_chess.place(x = 650, y = 100)
''''''
pieces_x = [i for i in range(32, 623, 42)]
pieces_y = [i for i in range(38, 629, 42)]

'''Print the chess board'''
#background
board = tk.Canvas(root_window, bg = "#F5DEB3", width = 640, height = 640)
#board.bind("<Button-1>", coorBack)  #对鼠标进行事件绑定，方便获取点击位置的坐标，下篇会用到
board.grid(row = 0, column = 0, rowspan = 6)
#line
for i in range(15):
    # Vertical Line
    board.create_line(32, (42 * i + 38), 622, (42 * i + 38))
    # Horizontal Line
    board.create_line((42 * i + 32), 38, (42 * i + 32), 628)
#point
point_x = [3, 3, 11, 11, 7]
point_y = [3, 11, 3, 11, 7]
for i in range(5):
    board.create_oval(42 * point_x[i] + 28, 42 * point_y[i] + 33, 42 * point_x[i] + 36, 42 * point_y[i] + 41, fill = "black")
# vertical coordinate in numbers
for i in range(15):
    label = tk.Label(board, text = str(i + 1), fg = "black", bg = "#F5DEB3", width = 2, anchor = tk.E)
    label.place(x = 2, y = 42 * i + 28)
# horizontal corrdinate in letters
count = 0
for i in range(65, 81):
    label = tk.Label(board, text = chr(i), fg = "black", bg = "#F5DEB3")
    label.place(x = 42 * count + 25, y = 2)
    count += 1

'''Set of intersection of lines'''
'''Each element is a 2-element array'''
intersection = []
for i in range(15):
    for j in range(15):
        intersection.append([(42 * i + 32),(42 * j + 38)])
    
# print(intersection[0][0])




#TODO Fix the function of tk
# banner = tk.Label(root_window, text='Choose Chess Color', font=('Times New Roman', 13), bg = "#F5DEB3").place(x=680, y=170, anchor='nw')
# on_hit = False
# CheckVar = tk.IntVar()
# black_choice = tk.Radiobutton(root_window, text="black", variable=CheckVar, value=1, anchor = 'w').place(x = 700, y = 200)
# white_choice = tk.Radiobutton(root_window, text="white", variable=CheckVar, value=2, anchor = 'w').place(x = 700, y= 230)
# if CheckVar.get() == "black" or CheckVar.get() == "white":
#     on_hit = True
#     color = CheckVar.get()
#     message = tkinter.messagebox.askokcancel(title = 'color', message = color)
# def getColor():
#     global color, on_hit, black_choice, white_choice
#     if on_hit:
#         ChessKind(color)

# def ChessKind(color):
#     global piece_color
#     piece_color = color
#     frames.delete("show_piece")
#     frames.create_oval(110 - PIECE_SIZE, 25 - PIECE_SIZE, 110 + PIECE_SIZE, 25 + PIECE_SIZE, fill = piece_color, tags = ("show_piece"))


'''
Mouse Click Event
<Button-1>  Left
<Button-2>  Right
<Double-Button-1>   Double Left Click
<Double-Button-2>   Double Right Click
'''
click_x = 0
click_y = 0

'''Return the coordinate of click'''
def click_cor(event):
    global click_x, click_y
    print(f"Left Click cooridinate:x= {event.x} y= {event.y}")
    click_x = event.x
    click_y = event.y
    ChessPos()        

'''Bind the mouse click with chess board'''
board.bind("<Button-1>", click_cor)
board.bind("<Double-Button-1>", click_cor)

'''Find the closest intersection of lines'''
def ChessPos():
    global click_x, click_y, person_chess, person_flag, pieces_x, pieces_y, intersection, piece_color
    putPiece(piece_color)
    #putPiece(piece_color)


'''Draw piece after find the chess position'''
def putPiece(piece_color):
    global axis_black, axis_white, click_x, click_y
    board.create_oval(click_x - PIECE_SIZE, click_y - PIECE_SIZE, click_x + PIECE_SIZE, click_y + PIECE_SIZE, fill = piece_color, tags = ("piece"))
    if piece_color == "white":
        axis_white.append([click_x, click_y])
        ChangeTurn("black")
    elif piece_color == "black":
        axis_black.append([click_x, click_y])
        ChangeTurn("white")
    #TODO Add the judge of game position: win to end/continues?  

def ChangeTurn(color):
    global piece_color, var, person_chess, frames
    piece_color = color
    frames.delete("show_piece")
    frames.create_oval(110 - PIECE_SIZE, 25 - PIECE_SIZE, 110 + PIECE_SIZE, 25 + PIECE_SIZE, fill = piece_color, tags = ("show_piece"))
    if color == "black":
        var.set("Your turn")
    elif color == "white":
        var.set("AI's turn")
    person_chess.destroy()
    person_chess = tk.Label(root_window, textvariable = var, width = 20, anchor = tk.CENTER, font = ("Times New Roman", 15) )
    person_chess.place(x = 650, y = 100)

root_window.mainloop()
