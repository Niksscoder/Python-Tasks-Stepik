'''

Write a program that takes as input a list of numbers on one line and displays on one line the values ​​that appear more
than once in it.

The sort method can be useful for solving this problem.

The displayed numbers should not be repeated, the order of their output can be arbitrary.

'''

# First way to solve this problem
a = list(map(int, input().split()))
first = a[0]
spis = []
if len(a) > 1:
  for i in a:
    print("It is a: ", i)
    sum = 0
    for j in a:
      if i == j:
        sum += 1
        if i not in spis and sum > 1:
          spis.append(i)

spis.sort()
print(*spis)


# Second way to solve this problem
numb = [int(i) for i in input().split()]
numb.sort()
n = []
for i in range(0,len(numb)-1):
    if numb[i] == numb[i+1]:
        n.append(numb[i])
        for i in range(0,len(n)-1):
            if n[i] == n[i + 1]:
                n.remove(n[i])
for list_out in n:
    print(list_out, end=' ')


# Third way to solve this problem
a = [int(i) for i in input().split()]
b = []

for i in range(len(a)):
    for j in range(len(a)-1):
        if j >= i:
            if a[i] == a[j+1] and a[i] not in b:
                b.append(a[i])
for i in range(len(b)):
    print(b[i], end=' ')