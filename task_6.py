'''
Write a program that reads a string with a number n,
which specifies the number of numbers to be counted. Next reads n
strings with numbers xi, one number on each line.
Total will be n + 1

'''

def f(x):
    return x ** 3

new_dict = {}
inputs = int(input())
for i in range(inputs):
    new_input = int(input())
    if new_input in new_dict:
        print(new_dict[new_input])
    else:
        new_dict[new_input] = f(new_input)
        print(new_dict[new_input])

