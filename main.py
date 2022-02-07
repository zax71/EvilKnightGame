import time, random

won = False

player = {
    "position": {"x": 1, "y": 1},
    "hotbar": [0, 0, 0],
    "health": random.randint(50, 100),
    "name": "ERROR"
}

def board(position):
  if position == {"x": 1, "y": 1}: # Start
    return "S"
  if position == {"x": 1, "y": 2}:
    return "1"
  if position == {"x": 1, "y": 3}:
    return "1"
  if position == {"x": 1, "y": 4}:
    return "D"
  if position == {"x": 2, "y": 2}:
    return "1"
  if position == {"x": 3, "y": 2}:
    return "1"
  if position == {"x": 3, "y": 3}:
    return "1"
  if position == {"x": 3, "y": 4}:
    return "1"
  if position == {"x": 3, "y": 5}:
    return "1"
  if position == {"x": 3, "y": 6}:
    return "1"
  if position == {"x": 4, "y": 6}:
    return "1"
  if position == {"x": 5, "y": 6}:
    return "1"
  if position == {"x": 6, "y": 6}:
    return "1"
  if position == {"x": 7, "y": 6}:
    return "1"
  if position == {"x": 8, "y": 6}:
    return "1"
  if position == {"x": 8, "y": 7}:
    return "1"
  if position == {"x": 8, "y": 8}:
    return "1"
  if position == {"x": 8, "y": 9}:
    return "E"
  if position == {"x": 6, "y": 5}:
    return "1"
  if position == {"x": 6, "y": 4}:
    return "1"
  if position == {"x": 7, "y": 4}:
    return "H"
  if position == {"x": 5, "y": 7}:
    return "1"
  if position == {"x": 5, "y": 8}:
    return "D"
  if position == {"x": 9, "y": 6}:
    return "D"
  else:
    return "0"

def welcome():
    print("========================================")
    print("Welcome to the Evil Knight Game")
    print("========================================\n")
    print("========================================")
    print("In this game the goal is to fight your way through a maze and defeat the boss!")
    print("In the maze you can walk on \"1\" characters, not on \"0\", the start and end are represented by \"S\" and \"E\" respectively")
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

def printBoard(player):
  # Make our dictionary easier to work with
  x = player["position"]["x"]
  y = player["position"]["y"]
  xy = player["position"]
  
  # Print out the board
  print(board({"x": x-1, "y": y+1}), end=" ")
  print(board({"x": x, "y": y+1}), end=" ")
  print(board({"x": x+1, "y": y+1}), end=" ")
  
  print()
  
  print(board({"x": x-1, "y": y}), end=" ")
  print(board({"x": x, "y": y}), end=" ")
  print(board({"x": x+1, "y": y}), end=" ")
  
  print()
  
  print(board({"x": x-1, "y": y-1}), end=" ")
  print(board({"x": x, "y": y-1}), end=" ")
  print(board({"x": x+1, "y": y-1}), end=" ")
  
  print()

def changeHealth(player, healthChange):
  if player["health"] > 100:
    player["health"] = 100
  
  if str(healthChange)[0] == "-":  
    player["health"] = player["health"]-healthChange[-1]
  else:
    player["health"] = player["health"]+healthChange[-1]
def move(player):
  direction = ""
  tmpxy = {
    "x": player["position"]["x"],
    "y": player["position"]["y"]
  }
  # Repeat until W A S or D
  while not direction in "WASD" or direction == "":
    direction = input("Type W A S or D to move in that direction ").upper()
  
  # Add distance to temp pos variable
  if direction == "W":
    tmpxy["y"] = tmpxy["y"]+1
  if direction == "A":
    tmpxy["x"] = tmpxy["x"]-1
  if direction == "S":
    tmpxy["y"] = tmpxy["y"]-1
  if direction == "D":
    tmpxy["x"] = tmpxy["x"]+1
  # Check if the move is legal
  
  if board(tmpxy) == "1":
    player["position"] = tmpxy
    print("moved")
  elif board(tmpxy) == "S":
    player["position"] = tmpxy
    print("start")
  elif board(tmpxy) == "E":
    player["position"] = tmpxy
    print("end")
  elif board(tmpxy) == "D":
    player["position"] = tmpxy
    print("damage (-3hp)")
    player["health"] = player["health"]-3
  elif board(tmpxy) == "H":
    player["position"] = tmpxy
    print("Heal (+2hp)")
    player["health"] = player["health"]+2
  else:
    print("no move")

def stats(player):
  print("Health: " + str(player["health"]))
  print("Hotbar: " + str(player["hotbar"]))

# Start game
welcome()
printBoard(player)
while True:
  move(player)
  printBoard(player)
  stats(player)
  if player["health"] > 100:
    player["health"] = 100
  elif player["health"] <= 0:
    break

if won == True:
  print("yay you won")
elif won == False:
  print("oof you died")