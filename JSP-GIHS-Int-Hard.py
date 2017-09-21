#!/usr/bin/env python

def timesTables(tableSize):
    tableStart = 1
    tableSize = tableSize + 1
    for i in range(tableStart, tableSize):
        for j in range(tableStart, tableSize):
            print('%d ' % (i * j), end='', flush=True)
        print('')

def oddTimesTables(tableSize):
    tableStart = 1
    tableSize = tableSize + 1
    for i in range(tableStart, tableSize, 2): # step by 2 to avoid events (1..3..5..etc.)
        for j in range(tableStart, tableSize, 2): # same as for i
            print('%d ' % (i * j), end='', flush=True)
        print('')

oddTimesTables(12)

