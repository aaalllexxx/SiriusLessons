l = [1, 2, 3, 15, 7, 9, 2, 6, 3]

for i in l:
    if l.count(i) > 1:
        print(True)
        exit()
print(False)