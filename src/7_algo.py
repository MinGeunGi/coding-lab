lists = [2, 4, 5, 1, 3]
for i in range(len(lists)-1):
    min_idx = i
    for j in range(i+1, len(lists)):
        if lists[j] < lists[min_idx]:
            min_idx = j

    lists[i], lists[min_idx] = lists[min_idx], lists[i]

print(lists)
