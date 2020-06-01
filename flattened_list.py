starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
abcd = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
flattened_list = []
x = len(starting_list)
while x != 0:
    for i in abcd[:x]:
        i = starting_list[0]
        starting_list.pop(0)
        x -= 1
        flattened_list.extend(i)
print(flattened_list)