import tkinter as tk
from tkinter import *

PIECE_SIZE = 10
piece_color = "black"

axis_black = []
axis_white = []

person_flag = 1
piece_color = "black"
color = "black"


#root window as chess board
root_window = tk.Tk()
root_window.title("Gomoku Game by Kevin Ye & Sihan Chen")
root_window.geometry("995x660")
root_window.resizable(0,0)
root_window.iconbitmap('./GomokuIcon.ico')


#chess info
frames = tk.Canvas(root_window, width=220, height=70)
frames.grid(row = 0, column = 1)
frames.create_oval(110 - PIECE_SIZE, 25 - PIECE_SIZE, 110 + PIECE_SIZE, 25 + PIECE_SIZE, fill = piece_color, tags = ("show_pieces"))
var = tk.StringVar()
var.set("Holding Black")
person_chess = tk.Label(root_window, textvariable = var, width = 20, anchor = tk.CENTER, font = ("Times New Roman", 15) )
person_chess.grid(row = 1, column = 1)
pieces_x = [i for i in range(32, 623, 42)]
pieces_y = [i for i in range(38, 629, 42)]

'''Print the chess board'''
#background
board = tk.Canvas(root_window, bg = "#F5DEB3", width = 640, height = 640)
#board.bind("<Button-1>", coorBack)  #对鼠标进行事件绑定，方便获取点击位置的坐标，下篇会用到
board.grid(row = 0, column = 0, rowspan = 6)
#line
for i in range(15):
    board.create_line(32, (42 * i + 38), 622, (42 * i + 38))
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

# banner = tk.Label(root_window, text='Choose Chess Color', font=('Times New Roman', 13), bg = "#F5DEB3").place(x=50, y=70, anchor='nw')
# on_hit = False
# CheckVar = tk.IntVar()
# black_choice = tk.Radiobutton(root_window, text="black", variable=CheckVar, value=1, anchor = 'w').place(x = 50, y = 100)
# white_choice = tk.Radiobutton(root_window, text="white", variable=CheckVar, value=2, anchor = 'w').place(x = 50, y= 130)
# if CheckVar.get() == "black" or CheckVar.get() == "white":
#     on_hit = True
#     color = CheckVar.get()
#     message = tkinter.messagebox.askokcancel(title = 'color', message = color)
# def getColor():
#     global color, on_hit, black_choice, white_choice
#     if on_hit:
#         ChessKind(color)

def ChessKind(color):
    global piece_color
    piece_color = color
    frames.delete("show_piece")
    frames.create_oval(110 - PIECE_SIZE, 25 - PIECE_SIZE, 110 + PIECE_SIZE, 25 + PIECE_SIZE, fill = piece_color, tags = ("show_piece"))



        


root_window.mainloop()
