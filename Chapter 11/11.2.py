#Looking inside of a file, Extracting numbers and summing them
name = input("Enter file:")  #Prompt User to input the file
if len(name) < 1 : name = "RegexRealSum.txt"   #Allows user to simply press enter to open specific file
handle = open(name) #assigns the file to a variable name
inp = handle.read() #Reads the entire file, newlines and all and puts it into a single string
import re #To use regular expressions in your program you must import the librARY
getnum = re.findall('[0-9]+', inp)  #Looks for integers using finaall and regular expressions from the string
getnumint = list(map(int, getnum)) #Map function interates through the list converting each string to an integer
sum = 0
for thing in getnumint:    #Simple definite loop to sum the parts of the list together
    sum = sum + thing
print(sum)   #Print Result
