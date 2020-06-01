x = []
for e in range(1, 129):
    x.append(e)
strt = 0
end = 8
for i in range(0, 16):
    print(*x[strt:end])
    strt = end
    end += 8
print()