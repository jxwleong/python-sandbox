import os
import xml.etree.ElementTree as ET


tree = ET.parse('sample.xml')
root = tree.getroot()
ET.dump(tree)
for child in root:
    print(child.tag, child.attrib)


for year in root.findall('year'):
    print(year.tag, year.attrib)

print(root[0][1].text)


def export_xml(tree, path):
    with open (path, 'wb') as f:
        tree.write(f)

export_xml(tree, os.path.join(os.getcwd(), 'writer.xml'))