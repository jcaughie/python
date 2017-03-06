t = 9.0
tot = 0;
for i in range(1000):
    for j in range(i):
        tot += 1;
        print(j);
print(tot)

##x = 3
##
##letters = ([chr(x) for x in range(97,123)])
###print(letters)
##for i in range(x):
##   print('-' * 2 * (x - i), end = '')
##   print(letters[(x - i - 1)])
   

##for i in range(x):
##   for j in range(4 * x - 3, -2):
##      print(letters[x - i - 1].center(x, '-'))
##   print(letters[x - i - 1].center(x * 3, '-'))
##for i in range(x - 1):
##   for j in range(4 * x - 3, -2):
##      print(letters[x - i - 1].center(x, '-'))
##   print(letters[x - i - 1].center(x * 3, '-'))


###!/bin/python3
##
##import sys
##
##arr = []
##for arr_i in range(6):
##   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
##   arr.append(arr_t)
###print(arr)
##
##maximum = 0
##firstPass = True
##for x in range(4):
##    topRow = arr[x]
##    midRow = arr[x + 1]
##    botRow = arr[x + 2]
##    for y in range(4):
####       print('top: ', sum(topRow[y:y+3]))
####       print('middle: ', midRow[y+1])
####       print('bottom: ',sum(botRow[y:y+3]))
####       print('='*15)
##       total = sum(topRow[y:y+3]) + midRow[y+1] + sum(botRow[y:y+3])
##       if firstPass:
##           maximum = total
##           firstPass = False
##       else:
##           maximum = max(maximum, total)
####       print(total)
##print(maximum)

##n =int(input('Enter number: '))
##b_value = (str(bin(n)))
###print(b_value)
##maximum = 0
##length = 0
##for x in range(2, len(b_value)):
##    #print(x)
##    #print(len(b_value))
##    #print('val: ' + b_value[x])
##    if int(b_value[x]) == 1:
##        length += 1
##        if x == len(b_value) - 1:
##            maximum = max(maximum, length)
##    else:
##        #print('max: ' + str(maximum))
##        maximum = max(maximum, length)
##        length = 0
##print(maximum)



#
## Enter your code here. Read input from STDIN. Print output to STDOUT
##X = int(input())
##Y = int(input())
##Z = int(input())
##N = int(input())
##A = []
##[ A.append([i,j,k]) for i in range(X+1) for j in range(Y+1) for k in range(Z+1) if i+j+k != N ]                
##print (A)

##import re
##
##str = 'an example word:cat!!'
##match = re.search(r'word:\w\w\w', str)
### If-statement after search() tests if it succeeded
##if match:
##    print ('found', match.group()) ## 'found word:cat')
##else:
##    print ('did not find')


##from decimal import *
##
##number = int(input())
##x = 0
##students = {}
##for x in range(number):
##    line = input().split()
##    name = line.pop(0)
##    students[name] = line

##student = input()
##average = 0
##for i in students[student]:
##    average += float(i)
##
##average = format(average/len(students[student]), '.2f')
##    
##print(average)
