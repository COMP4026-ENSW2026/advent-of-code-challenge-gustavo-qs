with open("sample.in", "r") as sample:

  lines = sample.read().splitlines()
  sum = 0
  i = 0
  first_line = ''
  second_line = ''
  third_line = ''

  lowercase_items = {chr(i): i-96 for i in range(97, 123)}
  uppercase_items = {chr(i): i-38 for i in range(65, 91)}

  for line in lines:
    if(i == 0): first_line = line
    elif(i == 1): second_line = line
    elif(i == 2): 
      third_line = line
      for char in first_line:
        if(char in second_line and char in third_line):
          if(char.islower()):
            sum += lowercase_items[char]
          else:
            sum += uppercase_items[char]
          break
      i = -1
    i += 1
  print(sum)