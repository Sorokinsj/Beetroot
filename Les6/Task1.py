from random import randint
i = 0
max = 0
List = list(range(10))
while i < 10:
    a = randint(0, 1000)
    List[i] = a
    if max < List[i]:
        max = List[i]
    i = i + 1
print(List, '\n', max)
