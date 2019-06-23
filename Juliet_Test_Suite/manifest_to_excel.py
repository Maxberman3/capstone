from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

columns=['path','flaw name','line']
DOMTree = xml.dom.minidom.parse("Juliet_Test_Suite/manifest.xml")
collection = DOMTree.documentElement
cases = collection.getElementsByTagName('testcase')
rowcount = 0
index=range(0,106372)
manifest=pd.DataFrame(index=index,columns=columns)
for case in cases:
    instances = case.getElementsByTagName('file')
    for instance in instances:
        filepath=instance.getAttribute('path')
        flaws=instance.getElementsByTagName('flaw')
        if len(flaws)>0:
            for flaw in flaws:
                name=flaw.getAttribute('name')
                line=flaw.getAttribute('line')
                manifest.set_value(rowcount,'path',filepath)
                manifest.set_value(rowcount,'flaw name',name)
                manifest.set_value(rowcount,'line',line)
                rowcount+=1
        else:
            manifest.set_value(rowcount,'path',filepath)
            rowcount+=1
xclwrite=ExcelWriter('manifest.xlsx')
manifest.to_excel(xclwrite,'Sheet 1',index=False)
xclwrite.save()
