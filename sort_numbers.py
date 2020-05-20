list1 = [2, 6, 1, 55, 4, 5, 13]
lenlst = len(list1)
sorted = []

while lenlst >= 1:
    for i in list1:
        i = list1[0]
    for e in list1[1:lenlst]:
        if i <= e:
            i = i
        if e < i:
            i = e
    sorted.append(i)
    list1.remove(i)
    lenlst -= 1
print(sorted)