count = 0
count2 = 0
for x in open('ANSW.txt', 'r').read().replace('\n\n', '\r').split('\r'):
    N = list(set(x.replace('\n', '')))
    count += len(N)
    a = x.split()
    for i in range(len(a)):
        a[i] = list(set(a[i]))
    for i in range(len(a[0])):
        checker = 1
        for j in range(1, len(a)):
            if a[0][i] in a[j]:
                checker += 1
        if checker == len(a):
            count2 += 1
print(count)
print(count2)
