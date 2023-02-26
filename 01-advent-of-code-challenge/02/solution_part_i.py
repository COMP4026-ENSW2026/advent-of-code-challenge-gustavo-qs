totalScore = 0

while True:
  try: 
    line = input()
    arr = line.split()
    enemy = arr[0]
    move = arr[1]

    if(enemy == "A"):
      if(move == "X"):
        totalScore += 4
      elif(move == "Y"):
        totalScore += 8
      else:
        totalScore += 3
    elif(enemy == "B"):
      if(move == "X"):
        totalScore += 1
      elif(move == "Y"):
        totalScore += 5
      else:
        totalScore += 9
    else:
      if(move == "X"):
        totalScore += 7
      elif(move == "Y"):
        totalScore += 2
      else:
        totalScore += 6
  except EOFError:
    print("total de pontos:", totalScore)
    break