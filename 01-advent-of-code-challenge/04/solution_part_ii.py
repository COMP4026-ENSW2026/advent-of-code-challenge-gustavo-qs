import sys

pairs = 0

for line in sys.stdin:
    left_elf = line.split(',')[0].split('-')
    right_elf = line.split(',')[1].split('-')

    if(int(left_elf[0]) <= int(right_elf[0]) and int(left_elf[1]) >= int(right_elf[0])):
        pairs += 1
    elif(int(right_elf[0]) <= int(left_elf[0]) and int(right_elf[1]) >= int(left_elf[0])):
        pairs += 1

print("ranges que contenham completamente seus pares:", pairs)