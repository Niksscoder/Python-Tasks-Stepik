'''Polindrome Task

if we can read a word from both sides, then this is a polindrome
'''

a = input()
i = 0
j = len(a)-1
is_Polindrom = True

while i < j:
    if a[i] != a[j]:
        is_Polindrom = False
    i += 1
    j -= 1
if is_Polindrom:
    print("YES")
else:
    print("NO")