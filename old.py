import time, random, keyboard

# Our board, 1 is a place you can go and 0 is a place you cannot go
board = [[5, 6, 7, 0, 0, 0, 0, 0, 0, 0],
         [8, 9, 10, 0, 1, 0, 0, 0, 0, 0],
         [11, 12, 13, 0, 1, 1, 0, 1, 0, 0],
         [0, 0, 1, 0, 0, 1, 1, 1, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 1, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 1, 1, 1, 1, 0, 1, 0],
         [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
         [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

player = {
    "position": {"x": 2, "y": 7},
    "hotbar": [0, 0, 0],
    "health": random.randint(50, 100),
    "name": "ERROR"
}

debouncer = False


def welcome():
    print("========================================")
    print("Welcome to the Evil Knight Game")
    print("========================================\n")
    print("========================================")
    print("In this game the goal is to fight your way through a maze and defeat the boss!")
    print("In the maze you can walk on \"1\" characters, not on \"0\" and your player is represented by a \"P\"")
    print("========================================\n")

def askName():
    inputtedName =""
    correct = False

    while correct == False:
        inputtedName = input("What would you like to name your knight? ")
        if inputtedName == "" or inputtedName[0] == " ":
            print("You must input a name!")
            correct = False
        else:
            correct = True
    return inputtedName

def visibleBoard(pos, board):

    outBoard = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

    outBoard[0][0] = board[pos["x"]-1][pos["y"]-1]
    outBoard[0][1] = board[pos["x"]-1][pos["y"]]
    outBoard[0][2] = board[pos["x"]-1][pos["y"]+1]

    outBoard[1][0] = board[pos["x"]][pos["y"]-1]
    outBoard[1][1] = "P"
    outBoard[1][2] = board[pos["x"]][pos["y"]+1]

    outBoard[2][0] = board[pos["x"]+1][pos["y"]-1]
    outBoard[2][1] = board[pos["x"]+1][pos["y"]]
    outBoard[2][2] = board[pos["x"]+1][pos["y"]+1]

    return outBoard

def print2DList(list):
    for row in list:
        for col in row:
            print(col, end=" ") # print each element separated by space
        print() # Add newline

def move():
    global player
    debouncer = False
    keyPressed = False
    while keyPressed == False:
        if keyboard.is_pressed("w"):
            if debouncer == False:
                print("W was pressed")
                player["position"]["y"] = player["position"]["x"]-1
                debouncer = True
                keyPressed = True
            else:
                debouncer = False

        if keyboard.is_pressed("a"):
                if debouncer == False:
                    print("A was pressed")
                    player["position"]["x"] = player["position"]["y"]+1
                    debouncer = True
                    keyPressed = True
                else:
                    debouncer = False

        if keyboard.is_pressed("s"):
                if debouncer == False:
                    print("S was pressed")
                    player["position"]["y"] = player["position"]["x"]+1
                    debouncer = True
                    keyPressed = True
                else:
                    debouncer = False

        if keyboard.is_pressed("d"):
                if debouncer == False:
                    print("D was pressed")
                    player["position"]["x"] = player["position"]["y"]-1
                    debouncer = True
                    keyPressed = True
                else:
                    debouncer = False



# Start game
welcome()

#player["name"] = askName()
print(player["name"], "is a nice name!\n")
print("Your random health value is", player["health"])


print2DList(visibleBoard(player["position"], board))

print("Press WAS or D to move")
print("Position:", player["position"])
while True:
    move()

    print2DList(visibleBoard(player["position"], board))
    print("Position:", player["position"])
    time.sleep(0.5)