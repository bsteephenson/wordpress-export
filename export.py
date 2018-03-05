
import xml

import xml.etree.ElementTree
root = xml.etree.ElementTree.parse('NAME_OF_XML_FILE.xml').getroot()


style = """

@import url('https://fonts.googleapis.com/css?family=Montserrat');

body { 
    font-family: 'Montserrat', sans-serif;
}

"""


print "<style>", style, "</style>"

for item in root.findall('.//item/content/..'):
    print "<h2>", item.find('title').text, "</h2>"
    print "<p>", item.find('pubDate').text, "</p>"
    print 
    print item.find('content').text
    print
    print
    
