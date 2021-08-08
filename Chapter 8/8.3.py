fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    stuff = fh.split()
    if stuff in list: continue
    else: lst.append(stuff)
    lst.append(fh)
lst.sort()
print(lst.rstrip())
