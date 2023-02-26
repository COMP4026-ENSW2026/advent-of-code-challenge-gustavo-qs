
#! X means you need to lose
#! Y means you need to end the round in a draw
#!  Z means you need to win.

#? (1 for Rock, 2 for Paper, and 3 for Scissors)
#? (0 if you lost, 3 if the round was a draw, and 6 if you won)

#! rock a
#! paper b
#! scissors c

totalScore = 0

while True:
  try: 
    line = input()
    arr = line.split()
    enemy = arr[0]
    move = arr[1]

    if(enemy == "A"):
      if(move == "X"):
        totalScore += 3
      elif(move == "Y"):
        totalScore += 4
      else:
        totalScore += 8
    elif(enemy == "B"):
      if(move == "X"):
        totalScore += 1
      elif(move == "Y"):
        totalScore += 5
      else:
        totalScore += 9
    else:
      if(move == "X"):
        totalScore += 2
      elif(move == "Y"):
        totalScore += 6
      else:
        totalScore += 7
  except EOFError:
    print("total de pontos:", totalScore)
    break
