List1 = list(range(1, 100))
List2 = []
ListEl = ['']
i1 = 0
i2 = 0
while i1 < len(List1):
    if List1[i1] % 7 == 0 and List1[i1] % 5 != 0:
        List2 = List2 + ListEl
        List2[i2] = List1[i1]
        i2 = i2 + 1
    i1 = i1 + 1
print('Extracting numbers =>', List2)