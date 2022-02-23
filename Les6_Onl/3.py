List1 = [1, 2, 3, 4, 9, 5, 6, 7]
List2 = [1, 2, 3, 4, 9, 5, 6, 7]
i = 0
while i < len(List1):
    List2[i] = List1[len(List1)-1-i]
    i = i + 1

print('List1 =', List1, '\n' 'List2 =', List2)
