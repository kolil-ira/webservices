import xml.etree.ElementTree as ET


xml_data = '''
<book>
    <title>the beginning after the end</title>
    <author>turtle me</author>
    <year>2024</year>
</book>
'''


root = ET.fromstring(xml_data)


title = root.find('title').text
author = root.find('author').text
year = root.find('year').text

print(f"Title: {title}")
print(f"Author: {author}")
print(f"Year: {year}")
