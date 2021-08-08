import urllib.request, urllib.parse, urllib.error #Since HTTP is s common urllib is a library that does all the socket work for us and makes web pages look like a file
import xml.etree.ElementTree as ET #Module implements a simple and efficient API for parsing and creating XML data.
import ssl  #Secure Sockets Layer, Designed to create secure connection between client and server.

api_key = False #An API key indentifies your app & your request for authorization and identification
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42 #Sample Data API key is 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ') #Enter URL to analyze
    if len(address) < 1: break #if no URL is entered break loop

    parms = dict()   #Create a dictionary named parms
    parms['address'] = address #Assigns the key value pair both as address within the dictionary
    if api_key is not False: parms['key'] = api_key #Assigns key value pair key with api_key
    url = serviceurl + urllib.parse.urlencode(parms) #Parse url into components & encodes to stop and charater escaping from URL
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx) #Reads the url through another vairable uh

    data = uh.read()  #Reads data in uh like a file
    print('Retrieved', len(data), 'characters') #Prints out Number of Characters in the data set
    print(data.decode()) #Decodes the string using the codec registered for the encoding, i.e. it defaults to the default string encoding
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)
