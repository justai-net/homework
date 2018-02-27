#!/usr/bin/env python2.7
columns = ['default', 'A', 'B', 'C', 'D', 'E']
value = ['default', 0, 0, 0, 0, 0]
index_columns = int(len(columns)) - 1
iterations = 0
print(value)
print('Current Location is ' + columns[iterations])
while True:             # Loop continuously
    inp = raw_input()   # Get the input
    if inp == 'F':
        if iterations < index_columns:
            print('F Command was received, moving to next column')
            iterations += 1
            print(iterations)
            print(index_columns)
        if iterations == index_columns:
            print('F Command was received, \
                  However Arm cannot move any further')
    if inp == 'R':
        print('R Command was received, returning to default position')
        iterations = 0
    if inp == 'D':
        if iterations > 0 and value[iterations] < 10:
            print('D was pressed')
            value[iterations] += 1
            if iterations < index_columns:
                iterations += 1
    for i in range(len(columns)):
        print('Arm location:' + columns[i],  value[i])
    print('Current Location is ' + columns[iterations])
    if inp == "kill":       # If it is a blank line...
        break
