import sys

lowercase_items = {chr(i): i-96 for i in range(97, 123)}
uppercase_items = {chr(i): i-38 for i in range(65, 91)}
sum = 0

for line in sys.stdin:
    a, b = line[:int(len(line)/2)], line[int(len(line)/2):]
    
    for char in a:
      if(char in b):
        if char.islower():
          sum += lowercase_items[char]
        else:
          sum += uppercase_items[char]
        break
print(sum)