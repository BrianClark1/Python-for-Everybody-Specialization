# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen #Since HTTP is s common urllib is a library that does all the socket work for us and makes web pages look like a file
from bs4 import BeautifulSoup  #Intializing BS
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') # Easy copy paste url in question
html = urlopen(url, context=ctx).read()  #Reads the url through another vairable html
soup = BeautifulSoup(html, "html.parser") #Deploys BS to works its magic
import re #To use regular expressions in your program you must import the library
sum = 0 #initializing the sum varibale for future use
# Retrieve all of the anchor tags
tags = soup('span')  #Parses the Document using BS to clean up the mess
for tag in tags:  #For each item in tags this loop, converts them to a string then uses RE extract the numerical digits for summing
    # Look at the parts of a tag
    y=str(tag)
    x= re.findall("[0-9]+",y) #Looks for integers using find all and regular expressions from the string [] the brackets indicate to take out any number for that range and the + means repeat the number
    for i in x: #Simple definite loop to sum the parts of the list together
        i=int(i) #Converts from string to integer in order t sum properl
        sum=sum+i #Summing statement
print(sum) #print out the answer
