l=[1,2,3,4,5]
if len(l) >= 2:
    l[0], l[-1] = l[-1], l[0]
print(l)
