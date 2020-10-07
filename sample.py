import copy

arr = [[1, 2, 3], [3, 4, 5], [5, 3, 2], [3, 13, 300]]
ans = []
arrNew = copy.copy(arr)
arrNew.pop(0)
for i in range(len(arr[0])):
    temp = arr[0][i]
    checker = []
    for elem in arrNew:
        if temp in elem:
            checker.append(True)
        else:
            checker.append(False)
    if not (False in checker):
        ans.append(temp)

print(ans)
