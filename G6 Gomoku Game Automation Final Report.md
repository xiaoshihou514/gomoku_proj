# Gomoku Game Automation Final Report

##  1. Introduction - Sihan

   Our team chose gomoku automation as our topic. First, I would like to introduce Gomoku to you. Gomoku is a simple turn-based game with 2 players using the $15\times15$ Go chessboard and chess pieces. It is a derivative of Go from Japan. Gomoku has an alias “*Five in A Row*” which clearly shows the rule of this game: once a player can make his/hers chess pieces “five in a row” horizontally, vertically, or diagonally, he/her wins the game. So at the beginning of our project, we decided to set the terminal position as one in which achieve five-in-a-row situation.

 

## 2. Algorithm -Kevin

### Algorithm-Main idea
   The main algorithm we used is a relatively simple one, we would iterate over every possible move and score them using predefined weights. To accelerate the process, we used individual threads to calculate the score of each possible move and remove the moves that seem less promising (i.e moves with lower scores). The program also consists of a special opening algorithm that uses a different set of weights optimised for the opening moves of the game.
### Algorithm-Program Flow
   The function search was the main function called from the front end. It is defined as follows:
```
def search(depth, current)
```
Where depth is the depth of the search and current is a 15x15 array consists of integers. $curent uses 0, 1 and 2 to represent blank space, friendly piece and enemy piece. 
The program is immediately followed by two for loops that would compute the score of possible moves (defined by having a neighbour in any direction) by calling:
```
def compute_score(current, x, y, cache):
   cache.append([compute_score_core(current, x, y),x,y])
```
Which would append the data in the given `cache` array.
In `compute_score_core(current, x, y)`, the program would search in all directions to find predefined patterns. The function uses brutal functional process to put all data in arrays and pass them to functions in the `pattern` file for further parsing. Which brings the program to 
```
def resolve_pattern_cont(pattern)
```
This part of the code would look for patterns that either is a pattern beneficial to us or prohibits further enemy moves and return a score. And finally `compute_score_core()` would return the final score.


## 3. Showcase - Sihan

   Here is Sihan Chen presenting the execution of code of Group 6. Here you can see that after we click the Run Code, the root window pops out. The major event of our code is mouse clicking. Once we click, there are 4 snippets of message being displayed: the accurate coordinate of clicking, the adjusted intersects coordinate, the coordinate in storing matrix of pieces which are converted by adjusted intersection coordinates, and the print out of the matrix. We set 1 to represent the first player and 2 to represent the second player. Let’s play without AI to show our judgement on winning. Let me just quickly win on the first player. Now, the function successfully figures out that there is a winner and knows who wins. Besides that, the frontend also blocks the mouse click after the game ends. Now we restart the game. And you can see that after the restart, the mouse clicking comes back.

Now let’s un-comment the implementation of AI and start a new game. Now you can see that I place the first chess piece in a random place. Then the AI will place right after me with one more click. According to the magnitude of depth, the calculating process will not be so quick. 

## 4. Problems and Solutions

### 4.1 Backend - Kevin

I have always used a normal text editor, like notepad, vscode or leafpad. But in this project I figured I would try sth different. I installed the neovim plugin on my vscode and forced myself to use it. It was hard, neovim was a modal editor and it has very different usage compared to a normal one. At first it was difficult to remember the keybindings but now having learned that I can edit my code much more efficiently. It was a nice tradeoff I would say.

At the beginning, I had not code with others once. That being said, the only git command I know was git clone. But now that I have to learn git, or it would be troublesome to share our progress. I flunked my files a couple times and completely broke my files twice. But hey, at least now I know how to git push -f.

Now the biggest challenge of all is debugging the entire project. I had the bad habit of debugging after finishing. So when I really begun to debug my files, it was like 500 lines of multi-threaded code. I had trouble tracing the code and I could hardly figure out why certain things happen. But with 50 lines of print statements added and a little vscode magic, I managed to make it work. I wrote the code in two days and spent two days debugging it. That has to be the hardest task for me in this project.

### 4.2 Frontend -Sihan

   The major problem in frontend development is to combine the frontend and backend. Since we divide parts during coding, our codes sometimes are not compatible. For example, we used different types of matrices to store chess pieces in the early coding process. Besides that, the order of UI display and AI calculation is also a problem. We debug so many times to adjust those points.

   The second problem is the function of the tkinter package. The poor support on child windows forces us to cancel the plan of achieving the function of choosing the type of chess. Thus, we have to assume that the human player plays the black chess.

## 5. Conclusion

### 5.1 Kevin's Conclusion

#### 5.1.1 Things learned

I would say the biggest thing I have learned is how to plan out a collaborative project. At first I had an idea of using pyo3 to use rust to write the algorithm and calling it using python code. But then more details of the project were drawn out and I aborted the idea. Another skill I learned is time management, we had great visions for this project but at the end only two thirds of it was implemented. It was sth that I should really pay attention to next time.

#### 5.1.2 Things achieved

But looking at the bright side, we created an entire python project without copying any external code, we created a github collaborative repo, we made this presentation possible and we wrote and tested lots of code. It’s definitely a great experience and I guess all of us had learned sth from it.

 

### 5.2 Sihan's Conclusion

   The most important thing I learned in this project is how to develop a relatively “complete” project with frontend and backend. This experience is valuable because I always do backend work in the previous class I’ve taken. Additionally, this experience profoundly enhanced my understanding of Python. Python opens a new window on coding/software engineering. It is so different from `Java`, `C++`. The thinking of problem solving via Machine Learning is also a gain. Using Machine Learning to find winning strategies and game positions instantaneously is so interesting and effective. All in all, this class and this project are great experiences.

 

## Appendix

##### Exploration: 

1. https://github.com/topics/gomoku-ai 
2. https://github.com/lihongxun945/gobang   

##### Documents read:

L. V. Allis, H. Jaap Van Den Herik, & M. P. H. Huntjens.(1994). Go-Moku and Threat-Space Search. *Computational Intelligence, 12*(1). https://www.researchgate.net/publication/2252447_Go-Moku_and_Threat-Space_Search

##### Our repository: 

https://github.com/Goproxer/gomoku_proj

##### Assets source:

[https://www.aigei.com/s?q=%E6%A3%8B&type=icon_7](https://www.aigei.com/s?q=棋&type=icon_7)
