import urllib.request, urllib.parse, urllib.error #Since HTTP is s common urllib is a library that does all the socket work for us and makes web pages look like a file
import json
import ssl  #Secure Sockets Layer, Designed to create secure connection between client and server.

serviceurl = 'http://py4e-data.dr-chuck.net/comments_1206241.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

readdata = urllib.request.urlopen(serviceurl, context=ctx) #Reads the url through another vairable
data = readdata.read().decode() #Officially reads the data from the URL and converts the bytes to strings
info = json.loads(data) #read the JSON document from file and The json. loads() is used to convert the JSON String document into the Python dictionary
totalSum = 0 #Intialize Sum
for count in info['comments']: #Instead of looping over the info dict. You want to loop over the info['comments'] dictionary specifically
    print(count["count"])
    totalSum = totalSum + (count["count"]) #Takes each individual count data and sums it
print(totalSum)
