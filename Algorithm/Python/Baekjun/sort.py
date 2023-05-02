lst = [(0, 0, 2), (2, 0, 2), (2, 2, 2), (0, 2, 3)]

lst.sort(key=lambda x, y:x[2], y[0])

print(lst)
