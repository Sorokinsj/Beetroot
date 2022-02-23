Tuple = (1, 2, 3, 4, 9, 5, 6, 7)
Sum = 0
i = 0
while i < len(Tuple):
    Sum = Sum + Tuple[i]
    i = i + 1
sr_zn = Sum / len(Tuple)
print('Tuple =', Tuple, '\n' 'average =', sr_zn)
