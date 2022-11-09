import requests
import xml.etree.ElementTree as ET

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