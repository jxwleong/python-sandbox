import os
import warnings

import xml.etree.ElementTree as ET

ROOT_DIR = os.path.join(os.getcwd())

print("Root DIR")
print(ROOT_DIR)
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

#export_xml(tree, os.path.join(ROOT_DIR, 'writer.xml'))

def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        warnings.warn('Invalid file path!', Warning)
#delete_file(os.path.join(ROOT_DIR, 'Edited.xml'))

delete_file('C:/ABC')