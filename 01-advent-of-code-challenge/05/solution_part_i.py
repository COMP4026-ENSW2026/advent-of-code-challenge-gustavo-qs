import sys

grid = []
col = { 1: 1, 2: 5, 3: 9, 4: 13, 5: 17, 6: 21, 7: 25, 8: 29, 9: 33 }
aux = True

for line in sys.stdin:
  if(line.strip() and aux):

    grid.append([char for char in line])
    inverted_grid = list(map(list, zip(*grid)))
    inverted_grid = [l[:-1] for l in inverted_grid]
    inverted_grid = [[c for c in row if c != ' '] for row in inverted_grid]

  else: 

    if(not line.strip()):
      aux = False
      continue

    else:

      move_qty = int(line.split()[1])
      move_from = int(line.split()[3])
      move_to = int(line.split()[5])

      for index, crater in enumerate(inverted_grid[col[move_from]][:move_qty]):
        inverted_grid[col[move_to]].insert(0, crater)         
        inverted_grid[col[move_from]][index] = ' '

      inverted_grid = [[c for c in row if c != ' '] for row in inverted_grid]

end_crates = ''

for i in range(1,10):
  end_crates += inverted_grid[col[i]][0]

print(end_crates)