
br = 0
first = 0
second = 0
third = 0
sum = 0


while True:
  try:
    line = input()
    if(line):
      if(br == 0):
        sum += int(line)
      else:
        sum = 0
        sum += int(line)
        br = 0      
    else: 
      if(first == 0):
        first = sum
      elif(first < sum):
        third = second
        second = first
        first = sum
      elif(second < sum):
        third = second
        second = sum
      elif(third < sum):
        third = sum
      br += 1
  except EOFError:
    print("soma dos 3 maiores:", first+second+third)
    break

