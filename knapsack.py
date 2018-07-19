#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value', 'juice'])
BUDGET = 100

def knapsack_solver(items, capacity):
  # !!!! IMPLEMENT ME
  items_to_select = []
  cost = 0
  value = 0
  for i in range(len(items)):
    if (cost + items[i][1]) <= BUDGET:
      cost += items[i][1]
      value += items[i][2]
      items_to_select.append(items[i][0])
    else:
      for remaining in range(i, len(items)-1):
        #print(items[remaining])
        if (cost + items[remaining+1][1]) <= BUDGET:
          cost += items[i+1][1]
          value += items[i+1][2]
          items_to_select.append(items[i][0])
        else:
          break
      return print(items_to_select, cost, value)
      

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2]), float(data[2])/float(data[1])))
    
    file_contents.close()

    ice_items = sorted(items, key=lambda item: item[3], reverse=True )
    #for i in range(len(ice_items)):
      #print(ice_items[i])
      
    print(knapsack_solver(ice_items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')


'''
PASS::
schwaaweb:Knapsack 02:58:09$ python knapsack.py data/medium2.txt 100
[155, 66, 10, 174, 188, 139, 28, 153, 145, 191, 120, 1, 64] 100 969
None
 
FAIL::
python knapsack.py data/medium1.txt 100
[104, 107, 134, 83, 44, 160, 60, 157, 77, 80, 94, 49, 117, 170] 91 1009
None

python knapsack.py data/medium3.txt 100
[170, 198, 15, 68, 133, 120, 158, 9, 47, 161, 116, 14, 164, 181, 154] 94 84
7                                                                         
None

python knapsack.py data/large1.txt 100
[104, 671, 737, 370, 432, 239, 107, 297, 561, 935, 796, 134, 693, 83, 949, 
704, 271, 782, 814, 566, 866, 420, 295, 795, 997, 44, 648, 623, 844, 160, 3
37, 907, 329, 909, 308, 335, 373, 913] 99 2628                            
None
'''
