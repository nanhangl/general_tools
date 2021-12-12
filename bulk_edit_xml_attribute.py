# the purpose of this script is to bulk edit an xml attribute

import glob, os
import xml.etree.ElementTree as ET

os.chdir("annotations_dir")
fileList = os.listdir()

for fileName in glob.glob("*.xml"):
    xmlTree = ET.parse(fileName)
    rootElement = xmlTree.getroot()
    objectElement = rootElement.find("object")
    nameElement = objectElement.find("name")
    nameElement.text = "stairs"
    xmlTree.write(fileName, encoding='UTF-8', xml_declaration=True)



