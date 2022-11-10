import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# Reading data from the xml file
with open('sponsorship-levels/blogs.2022-11-09.xml', 'r') as f:
	data = f.read()

# Passing the data of the xml
# file to the xml parser of
# beautifulsoup
data_b = BeautifulSoup(data, 'xml')

# A loop for replacing the value
# of attribute `test` to WHAT !!
# The tag is found by the clause
# `bs_data.find_all('child', {'name':'Frank'})`
for tag in data_b.find_all('child', {'team':'3D CAD Workshop - How to Model Almost Anything'}):
	tag['test'] = "WHAT !!"


# Output the contents of the
# modified xml file
print(bs_data.prettify())

def parseXML(xmlfile):
  
    # create element tree object
    tree = ET.parse(xmlfile)
  
    # get root element
    root = tree.getroot()
  
    # create empty list for news items
    newsitems = []
  
    # iterate news items
    for item in root.findall('./channel/item'):
  
        # empty news dictionary
        # news = {}
  
        # iterate child elements of item
        for child in item:
  
            # special checking for namespace object content:media
            if child.title == '':
                pass
            else:
                pass
  
        # append news dictionary to news items list
        newsitems.append()

  

def main():
  
  
    # parse xml file
    x = parseXML('topnewsfeed.xml')
if __name__ == "__main__":
  
    # calling main function
    main()