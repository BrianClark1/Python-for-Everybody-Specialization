# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
file = fh.read()
upperfile = file.upper()
print(upperfile.rstrip())
