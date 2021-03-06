'''
The simplest spelling checker can be based on 
a list of known words. 

If the entered word is not found in this list, 
it is marked as "error".

The first line is the number of d words known to us, 
after which on
d lines indicate these words. Then the number l of lines of text is passed to check, after which
l lines of text. 
'''

d = int(input())
spis_d = []
for i in range(d): # 4 (1, 2, 3, 4)
    for_d = input().lower()
    if for_d not in spis_d:
        spis_d.append(for_d)

l = int(input())
spis_l = []
for j in range(l):
    for_l = input().lower().split()
    for i in for_l:
        if i not in spis_d and i not in spis_l:
            spis_l.append(i)

print('\n'.join(spis_l))


# вывод ошибок 
# for i in spis_d:
#     print("word :", i)
#     for j in spis_l:
#         if i != j:
#             print("!= ", i)
#         else: print(j, end=" ")

# for i in spis_l: 
#     if i != spis_d[i]:
#         print(i)
     