fname = input("Enter file name: ")
fh = open(fname)
lst = list()
sfh = str(fh)
for line in sfh:
    stuff = sfh.split()
    if stuff not in lst:
        lst.append(stuff)
    else:
        continue
lst.sort()
print(lst)
