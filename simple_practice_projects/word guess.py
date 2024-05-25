a=[1, 2, 3, 4, 5]
b = [1,2,3]

for i in a:
    for j in b:
        if j!=i:
            a.append(j)
print(a)
