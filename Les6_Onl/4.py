List1 = [1, 2, 3, 4, 9, 5, 6, 7]
ListCop = []
ListEl = ['Element']
i = 0
while i < len(List1):
    ListCop = ListCop + ListEl
    ListCop[len(ListCop) - 1] = List1[i]
    i = i + 1
print('ListCopy =', ListCop)