from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

columns=['SourceFile','Bug Group','Bug Code','CWE ID','Bug Message','Build ID','AssesmentReportFile','Instance Location','Location ID','Primary','Explanation','StartLine','EndLine']
index=range(0,13494)
cppbugs=pd.DataFrame(index=index,columns=columns)
DOMTree = xml.dom.minidom.parse("sql_cpp.xml")
collection = DOMTree.documentElement
bugs=collection.getElementsByTagName('BugInstance')
rowcount=0
for bug in bugs:
    buglocations=bug.getElementsByTagName('BugLocations')
    cwe_reported=len(bug.getElementsByTagName('CweId'))
    if cwe_reported>0:
        cwe=bug.getElementsByTagName('CweId')[0].firstChild.nodeValue
    buggroup=bug.getElementsByTagName('BugGroup')[0].firstChild.nodeValue
    bugcode=bug.getElementsByTagName('BugCode')[0].firstChild.nodeValue
    bugmessage=bug.getElementsByTagName('BugMessage')[0].firstChild.nodeValue
    buildid=bug.getElementsByTagName('BugTrace')[0].getElementsByTagName('BuildId')[0].firstChild.nodeValue
    assessmentreportfile=bug.getElementsByTagName('BugTrace')[0].getElementsByTagName('AssessmentReportFile')[0].firstChild.nodeValue
    instancelocation=bug.getElementsByTagName('BugTrace')[0].getElementsByTagName('InstanceLocation')[0].firstChild.nodeValue
    for buglocation in buglocations:
        locations=buglocation.getElementsByTagName('Location')
        for location in locations:
            loc_id=location.getAttribute('id')
            is_primary=location.getAttribute('primary')
            sourcefile=location.getElementsByTagName('SourceFile')[0].firstChild.nodeValue
            startline=location.getElementsByTagName('StartLine')[0].firstChild.nodeValue
            endline=location.getElementsByTagName('EndLine')[0].firstChild.nodeValue
            explanation=location.getElementsByTagName('Explanation')[0].firstChild.nodeValue
            cppbugs.set_value(rowcount,'SourceFile',sourcefile)
            cppbugs.set_value(rowcount,'Bug Group',buggroup)
            cppbugs.set_value(rowcount,'Bug Code',bugcode)
            if cwe_reported>0:
                cppbugs.set_value(rowcount,'CWE ID',cwe)
            cppbugs.set_value(rowcount,'Bug Message',bugmessage)
            cppbugs.set_value(rowcount,'Build ID',buildid)
            cppbugs.set_value(rowcount,'AssessmentReportFile',assessmentreportfile)
            cppbugs.set_value(rowcount,'Instance Location',instancelocation)
            cppbugs.set_value(rowcount,'Location ID',loc_id)
            cppbugs.set_value(rowcount,'Primary',is_primary)
            cppbugs.set_value(rowcount,'Explanation',explanation)
            cppbugs.set_value(rowcount,'StartLine',startline)
            cppbugs.set_value(rowcount,'EndLine',endline)
            rowcount+=1
xclwrite=ExcelWriter('sql_cpp_bugs.xlsx')
cppbugs.to_excel(xclwrite,'Sheet 1',index=True)
xclwrite.save()
