#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value', 'juice'])

def knapsack_solver(items, capacity):
  # !!!! IMPLEMENT ME
  for i in range(len(items)):
    #print(items[i])
    pass

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
    for i in range(len(ice_items)):
      print(ice_items[i])
      
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')
