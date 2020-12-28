n = int(input())

sum = 0
if n < 2:
    print(n)
elif n == 2:
    print(1, 2)
else:
    for i in range(n):
        for j in range(i):
            if sum < n:
                print(i, end=" ")
                sum += 1
            else:
                break



