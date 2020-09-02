# import statements
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Get links
# URL of a WebPage
url = input("Enter URL: ") 

# Open the URL and read the whole page
html = urllib.request.urlopen(url).read()
# Parse the string
soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
# Returns a list of all the links
tags = soup('a')

#Prints all the links in the list tags
for tag in tags: 
  # Get the data from href key
  print(tag.get('href', None), end = "\n")