import os
import warnings

import xml.etree.ElementTree as ET

ROOT_DIR = os.path.join(os.getcwd())


def export_xml(tree, path):
    with open (path, 'wb') as f:
        tree.write(f)

#export_xml(tree, os.path.join(ROOT_DIR, 'writer.xml'))

def find_element(tree, tag):
    return tree.find(tag)

def update_element(element, value):
    element.text = value

print("Root DIR")
print(ROOT_DIR)
tree = ET.parse('sample.xml')
root = tree.getroot()
ET.dump(tree)

version = find_element(root, 'Version')
update_element(version, '3.20.542.1')
ET.dump(tree)
test_cfg = find_element(root, 'BSTATES')
print(find_element(tree, './TEST_CFG/AutoCfg/BSTATES').text)
# export_xml(tree, path=os.path.join(ROOT_DIR, "edited.xml"))


def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        warnings.warn('Invalid file path!', Warning)
#delete_file(os.path.join(ROOT_DIR, 'Edited.xml'))

#delete_file('C:/ABC')