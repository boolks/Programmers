alphabat = {'c=':1, 'c-':1, 'dz=':2, 'd-':1, 'lj':1, 'nj':1, 's=':1, 'z=':1}
first = ['c', 'd', 'l', 'n', 's', 'z']
word = input()
count = 0
tmp = ''
for i in range(len(word)):
    print(tmp)
    count += 1
    tmp += word[i]

    if tmp in alphabat:
        count -= alphabat[tmp]
        tmp = ''
    elif len(tmp) == 2:
        if tmp != 'dz':
            tmp = ''
        else:
            pass

print(count)
