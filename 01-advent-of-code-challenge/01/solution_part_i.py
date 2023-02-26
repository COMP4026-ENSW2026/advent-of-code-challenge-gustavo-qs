br = 0
higher = 0
sum = 0

while True:
  try:
    lines = input()
    if(lines):
      if(br == 0):
        sum += int(lines)
      else:
        sum = 0
        sum += int(lines)
        br = 0      
    else: 
      if(higher == 0):
        higher = sum
      elif(higher <= sum):
        higher = sum
      br += 1

  except EOFError:
    print("maior quantidade de calorias:", higher)
    break

