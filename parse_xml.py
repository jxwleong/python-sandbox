import xml.etree.ElementTree as ET


tree = ET.parse('sample.xml')
root = tree.getroot()

for child in root:
    print(child.tag, child.attrib)


for year in root.findall('year'):
    print(year.tag, year.attrib)

print(root[0][1].text)