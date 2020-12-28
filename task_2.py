
'''

Write a program that takes as input a list of numbers on one line. The program should output the sum of
its neighbors for each element of this list. For list elements that are extreme, one of the neighbors is the element
that is at the opposite end of this list.

For example, if the input is the list "1 3 5 6 10", then the output is the list "13 6 9 15 7" (without quotes).

If only one number came to the input, you must display it.
'''


spis_2 = []
n = list(map(int, input().split()))

sum = 0

if len(n) == 1:
    print(n[0])
else:
    for i in range(len(n)):
        if i == 0:
            sum = n[1] + n[-1]
            spis_2.append(sum)
        elif i == len(n)-1:
            sum = n[-2] + n[0]
            spis_2.append(sum)
        else:
            sum = int(n[i-1]) + int(n[i+1])
            spis_2.append(sum)
for i in spis_2:
    print(i, end=' ')



