'''

Learning that DNA is not a random string, computer science students who had just entered
the Institute of Bioinformatics suggested using a compression algorithm that compresses
repeated characters in a string.

Coding is done as follows:
s = 'aaaabbсaa' converted to a4b2с1a2 that is, groups of identical characters in the original string are replaced with
this character and the number of times it repeats at this position in the string.

Sample Input :
aaaabbcaa

Sample Output :
a4b2c1a2
'''



s = input()
lenth=len(s)
count = 1
for i in range(lenth):
    if i == lenth - 1:
        print(s[i] + str(count), end=" ")
    else:
        if s[i] == s[i+1]:
            count += 1
        else:
            print(s[i] + str(count), end=" ")
            count = 1