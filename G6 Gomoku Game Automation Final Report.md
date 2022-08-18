# Gomoku Game Automation Final Report

##  1. Introduction - Sihan

​	Gomoku is a turn-based game which is a derivative of Go from Japan. It takes 2 players and a $15\times 15$ square chessboard and black and white chess pieces. Gomoku has an alias “*Five in A Row*” which clearly shows the rule of this game: once a player can make his or hers chess pieces “five in a row” horizontally, vertically, or diagonally, he/her wins the game. So at the beginning of our project, we decided to set the terminal position as one in which achieve five-in-a-row situation. The goal of our project is achieving the automation of Gomoku.

### 1.1 Winning Strategy

​	According to the research, L. V. Allis et al.(1994) introduce the concept of threat sequences. A threat in Gomoku a position that a player will reach its N-Position if its opponent does not block it on a key spot. The threat sequence is consisted of continuous threats that is created by a player. Once a threat sequence is constructed, assume that player A creates it, the player B would have to block the player A so that the player B may not create its N-Position. The direct winning strategy is to create a double threat, either a straight four, or two separate threats, (L. V. Allis et al., 1994) in a threat sequence. Thus, the player A has 2 wining spots that no way the player B can block in the same time. 

​	The winning strategies are significant parts of gamming automation and it is certainly a goal of our project. In our project, we would like to concern about the effectiveness and the run time of the execution of algorithm of winning strategies.

## 2. Algorithm -Kevin

### 2.1 Main idea
   The main algorithm we used is a relatively simple one, we would iterate over every possible move and score them using predefined weights. To accelerate the process, we used individual threads to calculate the score of each possible move and remove the moves that seem less promising (i.e moves with lower scores). The program also consists of a special opening algorithm that uses a different set of weights optimised for the opening moves of the game.
### 2.2 Program Flow
   The function search was the main function called from the front end. It is defined as follows:
```python
def search(depth, current)
```
Where depth is the depth of the search and current is a 15x15 array consists of integers. $curent uses 0, 1 and 2 to represent blank space, friendly piece and enemy piece. 
The program is immediately followed by two for loops that would compute the score of possible moves (defined by having a neighbour in any direction) by calling:
```python
def compute_score(current, x, y, cache):
   cache.append([compute_score_core(current, x, y),x,y])
```
Which would append the data in the given `cache` array.
In `compute_score_core(current, x, y)`, the program would search in all directions to find predefined patterns. The function uses brutal functional process to put all data in arrays and pass them to functions in the `pattern` file for further parsing. Which brings the program to 

```python
def resolve_pattern_cont(pattern)
```
This part of the code would look for patterns that either is a pattern beneficial to us or prohibits further enemy moves and return a score. And finally `compute_score_core()` would return the final score. Which would bring us back to the original search function.
Now `$tree` is full of scored moves, so we check if `$depth` is equal to 1 (either a search with depth 1 or called recursively by another `search` instacne), in which case we would simply return the move with the largest score.
If that is not the case, the search function would find the best enemy move after each possible move we have made. This is done by iterating over `$tree` and using  `def commit_move(x, y, current)` to create a new instance of `$current`, and we would use a similar precess like earlier to compute the best enemy move. The process involves
```python
def compute_score_rev(current, x, y, cache)

compute_score_rev_core(current, x, y)

def resolve_pattern_cont_rev(pattern)
```
which all use similiar procedures to the original duntion.
After all results were collected, we would decrease `$depth` by 2 and call `def search(depth, current)` again to get the overall best score, and finally iterating over every move to find the maximum score to return to the front end.

### 2.3 Opening Moves
   If you recall from earlier, the opening moves were made by a different algorithm.

## 3. Frontend - Sihan

### 3.1 UI and Functions

   The construction of frontend implements the `tkinter` package from Python libraries. There are 3 core functions with the support of `tkinter` package. The first one the painting of chessboard and chess pieces. The implementing of class `Canvas` and method `created_line` paints the chessboard with lines. We use `create_oval` to paint the star points and chess pieces. The second one is listening the mouse click event with `bind` method. Thus, we can get an accurate coordinate of each clicking on board. By using `math` package, we can calculate the closest intersection of lines on board and return to the `creat_oval` method to draw piece precisely.  The third one is the ability to play more than one game in each run of code. We achieve this function by adding the "reset" button. Once the algorithm of game position figures out a winner, the mouse clicking event and chess board will be `unbind`(the root window still binds the event), i.e. no more chess can be put on board. Players can only either close this run or click the "reset" button. In the `def gameReset()`, we define that once the "reset" is clicked, all variables will be turned back to default state: 

```python
def gameReset():
    global store_chess, piece_color, person_flag, intersection, board,step_count
    var.set("Holding Black")      
    win_message.set("")
    end_message.set("")         
    ChangeTurn("black")             
    board.delete("piece")
    store_chess = [[0 for i in range(15)] for j in range(15)]
    piece_color = "black"
    person_flag = 0
    board.bind("<Button-1>", click_cor)
    step_count = 0
```

### 3.2 Data Structure

​	The essential data structure is a double matrix:

```python
store_chess = [[0 for i in range(15)] for j in range(15)]
```

​	The initial state is `0`, the black chess pieces are represented by `1`, and the white chess pieces are represented by `2`. Once a coordinate of intersection that chesses are put is return, we use calculation to transfer `(x,y)` into `(rows, cols)` and change a number according to color. Once the "reset" button is clicked, the matrix will be reset to the initial state.

## 4. Problems and Solutions

### 4.1 On Backend - Kevin

I have always used a normal text editor, like notepad, vscode or leafpad. But in this project I figured I would try sth different. I installed the neovim plugin on my vscode and forced myself to use it. It was hard, neovim was a modal editor and it has very different usage compared to a normal one. At first it was difficult to remember the keybindings but now having learned that I can edit my code much more efficiently. It was a nice tradeoff I would say.

At the beginning, I had not code with others once. That being said, the only git command I know was git clone. But now that I have to learn git, or it would be troublesome to share our progress. I flunked my files a couple times and completely broke my files twice. But hey, at least now I know how to git push -f.

Now the biggest challenge of all is debugging the entire project. I had the bad habit of debugging after finishing. So when I really begun to debug my files, it was like 500 lines of multi-threaded code. I had trouble tracing the code and I could hardly figure out why certain things happen. But with 50 lines of print statements added and a little vscode magic, I managed to make it work. I wrote the code in two days and spent two days debugging it. That has to be the hardest task for me in this project.

### 4.2 On Frontend -  Sihan

   The major problem in frontend development is to combine the frontend and backend. Since we divide parts during coding, our codes sometimes are not compatible. For example, we used different types of matrices to store chess pieces in the early coding process. Besides that, the order of UI display and AI calculation is also a problem. We debug so many times to adjust those points.

   The second problem is the function of the `tkinter` package. The poor support on child windows forces us to cancel the plan of achieving the function of choosing the type of chess. Thus, we have to assume that the human player plays the black chess.

## 5. Conclusion

### 5.1 Kevin's Conclusion

#### 5.1.1 Things learned

I would say the biggest thing I have learned is how to plan out a collaborative project. At first I had an idea of using pyo3 to use rust to write the algorithm and calling it using python code. But then more details of the project were drawn out and I aborted the idea. Another skill I learned is time management, we had great visions for this project but at the end only two thirds of it was implemented. It was sth that I should really pay attention to next time.

#### 5.1.2 Things achieved

But looking at the bright side, we created an entire python project without copying any external code, we created a GitHub collaborative repo, we made this presentation possible and we wrote and tested lots of code. It’s definitely a great experience and I guess all of us had learned something from it.

 

### 5.2 Sihan's Conclusion

   The most important thing that I learned in this project is how to develop a relatively “complete” project with frontend and backend. This experience is valuable because I always do backend work in the previous class I’ve taken. Additionally, this experience profoundly enhanced my understanding of `Python`. Python opens a new window on coding/software engineering. It is so different from `Java`, `C++`. The thinking of problem solving via Machine Learning is also a gain. Using Machine Learning to find winning strategies and game positions instantaneously is so interesting and effective. All in all, this class and this project are great experiences.

 

## Appendix

##### Exploration

1. https://github.com/topics/gomoku-ai 
2. https://github.com/lihongxun945/gobang   

##### Documents Read:

L. V. Allis, H. Jaap Van Den Herik, & M. P. H. Huntjens.(1994). Go-Moku and Threat-Space Search. *Computational Intelligence, 12*(1). https://www.researchgate.net/publication/2252447_Go-Moku_and_Threat-Space_Search

##### Our Repository

https://github.com/Goproxer/gomoku_proj

##### Assets Source

[https://www.aigei.com/s?q=%E6%A3%8B&type=icon_7](https://www.aigei.com/s?q=棋&type=icon_7)
