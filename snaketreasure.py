
import random
import time 
from threading import Thread
 
import msvcrt as m # enabling to use keys on the keyboard
 
# Basic values setting
snake_head = ">"
body = "@"
x = 5
y = 3
game_thread = True
coin_x = 5
coin_y = 6
button_default = "d"
score = 0
last2X = 0; last2Y = 0
lastX = 0; lastY = 0
elemX = [0 for i in range(100)]; elemY = [0 for i in range(100)]
 
# after the new board appears clear the previous ones
import os
def clear():  # after updating the new board onscreen to clear the previous ones
    for i in ["cls", "clear"]:
        os.system(i)
        break
 
 
def board(width: int = 30, height: int = 15, cell_x: int = x, cell_y: int = y):
    global score, coin_x, coin_y, game_thread, snake_head, last2X, lastX, lastY, last2Y, elemY, elemX
    clear()
    for i in range(height):
        for j in range(width):
            if cell_x == coin_x and cell_y == coin_y:
                coin_x = random.randint(2, width-1)
                coin_y = random.randint(2, height-1)
                score += 1
                # conditions for ending the game: if the frame is touched
            
 
            if not(x in range(width-39)) and not(y in range(height-1)) or not(x in range(width-1)) and not(y in range(height-15)):
                print(f"\nGAME OVER\nScore: {score}")
                game_thread = False
                exit()          
 
            if j == 0:
                print('*', end='')  
            elif i == 0:
                print('*', end='')
            elif i == height-1:
                print('*', end='')
            elif j == width-1:
                print('*', end='')
            elif cell_x == j and cell_y == i:
                print(snake_head, end='')
            elif coin_x == j and coin_y == i:
                print("$", end='')
            else:
                pr = True
                for ls in range(score):
                    if elemX[ls] == j and elemY[ls] == i:
                        print(body, end="")
                        pr = False
                if pr: print(' ', end='')
 
        print()
    
    
    print(f"Score: {score}\n\tArrows - move\n\t\tESC - exit")
    lastX = cell_x; lastY = cell_y
    if score > 0:
        for el in range(score):
            last2X = elemX[el]; last2Y = elemY[el]
            elemX[el] = lastX; elemY[el] = lastY
            lastX = last2X; lastY = last2Y
 # using keyboard buttons to move our snake
def button_move():  
    global button_default
    while game_thread:
        button_default = m.getch()[0]  
 
def move(): 
    global x, y, game_thread, button_default, snake_head
 
    while game_thread:   # the symbol changing the direction of an arrow of the snakehead
        if button_default in [""," "]: button_default = "d"
        elif button_default in ["w", 119, 230, 72]: y -= 1; snake_head = "^"
        elif button_default in ["a", 97, 228, 75]: x -= 1; snake_head = "<"
        elif button_default in ["s", 115, 235, 80]: y += 1; snake_head = "v"
        elif button_default in ["d", 100, 162, 77]: x += 1; snake_head = ">"
 
        elif button_default in ["exit", 27]:
            print("you exit the game")
            game_thread = False
            exit()
 
        board(cell_x=x, cell_y=y)
            # set the speed of the snake movement
        time.sleep(.2)
 
 
def main():
    board()
    Thread(target=move).start()
    Thread(target=button_move).start()
 
if __name__ == "__main__":
    
    main()
