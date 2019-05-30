from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

columns=['SourceFile','Bug Group','Bug Code','Bug Severity','Bug Message','Build ID','AssesmentReportFile','Instance Location','Location ID','Primary','StartLine','EndLine']
index=range(0,865)
parasoftbugs=pd.DataFrame(index=index,columns=columns)
DOMTree = xml.dom.minidom.parse("sql_parasoft.xml")
collection = DOMTree.documentElement
bugs=collection.getElementsByTagName('BugInstance')
rowcount=0
for bug in bugs:
    buglocations=bug.getElementsByTagName('BugLocations')
    buggroup=bug.getElementsByTagName('BugGroup')[0].firstChild.nodeValue
    bugcode=bug.getElementsByTagName('BugCode')[0].firstChild.nodeValue
    bugseverity=bug.getElementsByTagName('BugSeverity')[0].firstChild.nodeValue
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
            parasoftbugs.set_value(rowcount,'SourceFile',sourcefile)
            parasoftbugs.set_value(rowcount,'Bug Group',buggroup)
            parasoftbugs.set_value(rowcount,'Bug Code',bugcode)
            parasoftbugs.set_value(rowcount,'Bug Severity',bugseverity)
            parasoftbugs.set_value(rowcount,'Bug Message',bugmessage)
            parasoftbugs.set_value(rowcount,'Build ID',buildid)
            parasoftbugs.set_value(rowcount,'AssessmentReportFile',assessmentreportfile)
            parasoftbugs.set_value(rowcount,'Instance Location',instancelocation)
            parasoftbugs.set_value(rowcount,'Location ID',loc_id)
            parasoftbugs.set_value(rowcount,'Primary',is_primary)
            parasoftbugs.set_value(rowcount,'StartLine',startline)
            parasoftbugs.set_value(rowcount,'EndLine',endline)
            # if location.hasElement('EndLine'):
            #     endline=location.getElementsByTagName('EndLine')[0].firstChild.nodeValue
            #     parasoftbugs.set_value(rowcount,'EndLine',endline)
            rowcount+=1
xclwrite=ExcelWriter('sql_sonar_bugs.xlsx')
parasoftbugs.to_excel(xclwrite,'Sheet 1',index=True)
xclwrite.save()
