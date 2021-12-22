import random as rand


B_list = list(range(1, 16))
I_list = list(range(16, 31))
N_list = list(range(31, 46))
G_list = list(range(46, 61))
O_list = list(range(61, 76))


def generate_board():
  board = []
  b = B_list.copy()
  i = I_list.copy()
  n = N_list.copy()
  g = G_list.copy()
  o = O_list.copy()
  for j in range(5):
    l = []
    l.append(b.pop(rand.randint(1, len(b))))
    l.append(i.pop(rand.randint(1, len(b))))
    l.append(n.pop(rand.randint(1, len(b))))
    l.append(g.pop(rand.randint(1, len(b))))
    l.append(o.pop(rand.randint(1, len(b))))
    #might need to fix the number spread (why is there a -1 on b but not the rest)
    board.append(l)
  board[2][2] = "X"
  return board


def bingo_letter(roll):
  if roll in B_list:
    return "B " + str(roll)
  elif roll in I_list:
    return "I " + str(roll)
  elif roll in N_list:
    return "N " + str(roll)
  elif roll in G_list:
    return "G " + str(roll)
  else:
    return "O " + str(roll)


def is_bingo(board):
  if ["X"] * 5 in board:
    return True
  if board[0][0] == "X" and board[0][4] == "X" and board[4][0] == "X" and \
  board[4][4] == "X":
    return True
  c1 = []
  c2 = []
  l1 = []
  l2 = []
  l3 = []
  l4 = []
  l5 = []
  for i in range(5):
    c1.append(board[i][i])
    c2.append(board[i][4 - i])
    l1.append(board[i][0])
    l2.append(board[i][1])
    l3.append(board[i][2])
    l4.append(board[i][3])
    l5.append(board[i][4])
  if c1 == ["X"] * 5 or c2 == ["X"] * 5 or l1 == ["X"] * 5 or l2 == [
    "X"] * 5 or l3 == ["X"] * 5 or l4 == ["X"] * 5 or l5 == ["X"] * 5:
    return True
  return False


def has_bingo(boards):
  for i in range(len(boards)):
    if is_bingo(boards[i]):
      return True
  return False


def print_board(board):
  for i in range(5):
    for j in board[i]:
      if len(str(j)) == 1:
        print(" " + str(j) + " ", end = " ")
      else:
        print(str(j) + " ", end = " ")
    print()
  return None


def print_boards(boards):
  for row in range(5):
    print("  ", end = "")
    for board in boards:
      for j in board[row]:
        if len(str(j)) == 1:
          print(" " + str(j) + " ", end = " ")
        else:
          print(str(j) + " ", end = " ")
      print(" | ", end = " ")
    print()
  return None


def game():
  gen = generate_boards()
  boards = gen[0]
  names = gen[1]
  board_list = list(range(1, 76))
  game_length = 0
  called = []
  while not has_bingo(boards):
    input("Hit Return to roll!")
    print("============")
    roll = board_list.pop(rand.randint(1, len(board_list) - 1))
    called.append(roll)
    print(bingo_letter(roll))
    game_length += 1
    print("============")
    hits = []
    for k in range(len(boards)):
      for i in range(5):
        if roll in boards[k][i]:
          boards[k][i][boards[k][i].index(roll)] = "X"
          hits.append(names[k])
    if hits != []:
      print("On the boards of player(s): ", end = " ")
    for p in range(len(hits)):
      print(hits[p], end = " ")
    print()
    for i in range(len(boards)):
      print(names[i] + " " * (23 - len(names[i])), end = " ")
    print()
    print_boards(boards)
  for i in range(len(boards)):
    if is_bingo(boards[i]):
      print(names[i] + " has won! Balls rolled: " + str(game_length))
  return None


def bingo_rolls():
  board_list = list(range(1, 76))
  game_length = 0
  while game_length < 74:
    print("============")
    game_length += 1
    print(str(game_length) + ":", end = ' ')
    roll = board_list.pop(rand.randint(1, len(board_list) - 1))
    print(bingo_letter(roll))
    print("============")
    t = input("Type Y if there is a bingo, or Return if there isn't!")
    if t == "Y":
      return None
  print("How did you get here?")
  return None


def generate_boards():
  amount = input(
    "Type in an amount from 1-7 to generate that number of cards: ")
  allowed_inputs = ["1", "2", "3", "4", "5", "6", "7"]
  if amount not in allowed_inputs:
    return generate_boards()
  print("Write the names of the players (max 22 characters)!")
  names = []
  j = 0
  while j < int(amount):
    name = input("Player " + str(j + 1) + ": ")
    if len(name) <= 22:
      names.append(name)
      j += 1
  boards = []
  for i in range(int(amount)):
    boards.append(generate_board())
    print(names[i] + " " * (23 - len(names[i])), end = " ")
  print()
  print_boards(boards)
  return [boards, names]

while True:
  generate_boards()

