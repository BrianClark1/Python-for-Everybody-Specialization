# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
added = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    pos = line.find(':')
    value = line[pos+1:]
    fvalue = float(value)
    added = added + fvalue
answer = added/count
print("Average spam confidence:"answer)






#text = "X-DSPAM-Confidence:    0.8475";
#atpos = text.find(':    0.')
#value = text[atpos:atpos+6]
#fvalue = float(value)
#print(value)
