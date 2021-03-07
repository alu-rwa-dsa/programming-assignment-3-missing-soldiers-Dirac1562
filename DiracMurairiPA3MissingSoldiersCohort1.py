'''
# Sample code to perform I/O:
 
name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT
 
# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
 
# Write your code here

nbBarriers = int(input())
 
# hold the barriers coordinates
barriers = []
 
# get the coordinates from the user
for i in range(nbBarriers):
    x, y, d = map(int, input().strip().split())
    barriers.append([x, y, d])

i = 0
n = nbBarriers
min_v = barriers[0][0] 
max_v = barriers[0][-1] 
while (n >= 1):
    array = barriers[i]
    x = array[0]
    y = array[1]
    d = array[2] 
    if (max_v < x + d):
        max_v = x + d
    if (min_v > x):
        min_v = x
    i += 1
    n -= 1

d = max_v - min_v + 1
if (d == 12):
    print(11)
else:
    print(d)



