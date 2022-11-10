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
  
        # getting new title items into dictionary
        new_item = {}
  
        # iterate child elements of item
        for child in item:
            
            # # special checking for namespace object content:media
            if child.title == 'title':
                new_item.append(child.title)
            else:
                print('Null')
  
        
            

  

def main():
    # parse xml file
    x = parseXML('blogs.2022-09-21.xml')
if __name__ == "__main__":
  
    # calling main function
    main()