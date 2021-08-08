name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
bigbag = dict()
count = 0
for line in handle:
    emails = line.split()
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
            need = emails[1]
            bigbag[need] = bigbag.get(need,0) + 1
mostpopvalue = 0
for k,v in bigbag.items():
    if v > mostpopvalue:
        mostpopvalue=v
        mostpopkey=k
print(mostpopkey,mostpopvalue)
#mostpopkey = None
#mostpopvalue = None
#for need.count in bigbag.items():
#    if mostpopkey is None or count > mostpopkey:
#        mostpopvalue  = word
#        mostpopvalue = count
#print(mostpopkey,mostpopvalue)
