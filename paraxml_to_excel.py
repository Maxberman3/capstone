from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd

columns=[]
DOMTree = xml.dom.minidom.parse("parasoft.xml")
collection = DOMTree.documentElement
bugs=collection.getElementsByTagName('BugInstance')
print(len(bugs))
