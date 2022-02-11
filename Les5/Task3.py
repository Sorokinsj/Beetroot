from random import shuffle
s=input()
l=list(s)
i = 1
while i <= 5:
    shuffle(l)
    print ("Вывод перемешанного списка ", l)
    i = i + 1