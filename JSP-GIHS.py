#!/usr/bin/env python

def timesTables(tableSize):
    tableStart = 1
    tableSize = tableSize + 1
    for i in range(tableStart, tableSize):
        for j in range(tableStart, tableSize):
            print('%d ' % (i * j), end='', flush=True)
        print('')

timesTables(12)
