from random import randint
i = 0
List1 = list(range(10))
List2 = list(range(10))
List3 = []
ListEl = ['Element']
while i < 10:
    a = randint(1, 10)
    List1[i] = a
    b = randint(1, 10)
    List2[i] = b
    i = i + 1
i1 = 0
i2 = 0
i3 = 0
while i1 < len(List1):
    while i2 < len(List2):
        if List1[i1] == List2[i2]:
            List3 = List3 + ListEl
            List3[i3] = List1[i1]
            i3 = i3 + 1
        i2 += 1
    i2 = 0
    i1 += 1
List3 = list(set(List3))
print(List1)
print(List2)
print(List3)