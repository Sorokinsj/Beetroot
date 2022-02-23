list = [1, 2, 3, 4, 9, 5, 6, 7]
i = 1
max = list[0]
while i < len(list):
    if max < list[i]:
      max = list[i]
    i = i+1
print('list =',list,'\n' 'Max of list =',max)

