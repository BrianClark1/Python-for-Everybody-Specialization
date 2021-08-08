name = input("Enter file:") #Prompt User to input the file
if len(name) < 1 : name = "mbox-short.txt"  #Allows user to simply press enter to open specific file
handle = open(name) #assigns the file to a variable name
timesheet = dict()   # Creates a dictionary to store the times & Counts
for line in handle: #Creating a for loop to search through the file line by line
    line = line.rstrip()
    finder = line.split()  #Creates a variable that splits each line into a list
    if line.startswith('From:'): # If statement to avoid lines that start with from but include no semicolon
        continue    # Prompts to continue to next if statement
    if line.startswith('From'):   # Lines that begin with 'From:' include the information that we are looking for
            time = finder[5]  # This parses the time string out of the list
            realtime = time[0:2]  #this takes out the our from the time string
            timesheet[realtime] = timesheet.get(realtime,0) + 1    #Usng the get method to check to see if a key is already in a dictionary, and assuming a defualt value if the key is not there & then counts it.
prefinal = timesheet.items()   #The items() method in dictionaries returns a list of (key, value) tuples
final = sorted(prefinal)  #the sorted() function sorts a list of tuples to get a sorted version of a dictionary
for item in final:
    print(*item)   #Prints each item in the list independently the star unravels the tuple during the call to print
