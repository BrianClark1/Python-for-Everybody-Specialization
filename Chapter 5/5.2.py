largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        fnum = float(num)
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest = fnum
    if largest is None:
        largest = fnum
    if fnum > largest :
        largest = fnum
    if fnum < smallest :
        smallest = fnum
Ilargest = int(largest)
Ismallest = int(smallest)
print("Maximum is", Ilargest)
print("Minumum is", Ismallest)
