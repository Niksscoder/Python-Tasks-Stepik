'''

When Pavel was in school, he memorized the multiplication table with rectangular blocks.
For training, a program that would show a block of the multiplication table would be very useful to him.

Write a program that takes four numbers a, b, c, and d as input, each on its own line.
The program should display a fragment of the multiplication table for all numbers of the segment [a;b]
to all numbers of the segment[c;d]

'''


a = int(input())
b = int(input())
c = int(input())
d = int(input())
for x in range(c, d + 1):
    print('\t', x, end=" ")
print()
for i in range(a, b+1):
    print(i, end=" ")
    for j in range(c, d +1):
        print('\t', i * j, end=" ")
    print()



