import pandas as pd
from pandas import ExcelWriter,ExcelFile

alerts=pd.read_excel('Juliet_Test_Suite/swampresults_edit_checked.xlsx')
data=pd.DataFrame(columns=['Severity','CWE','Clang Alert','CodeSonar Alert','Clang Rule','CodeSonar Rule','Line','True Positive'])
indexmap={}
for index,row in alerts.iterrows():
    print(index)
    alertpath=row['Path']
    severity=row['Severity']
    cwe=row['CWE']
    rule=row['Rule']
    line=row['Line']
    positive=row['True Positive Flag']
    tool=row['Tool']
    if alertpath not in indexmap:
        indexmap[alertpath]={line:index}
        if tool=='Clang':
            data=data.append({'Severity':severity,'CWE':cwe,'Clang Alert':1,'CodeSonar Alert':0,'Clang Rule':rule,'CodeSonar Rule':'N/A','Line':line,'True Positive':positive},ignore_index=True)
        elif tool=='gt-csonar':
            data=data.append({'Severity':'N/A','CWE':'N/A','Clang Alert':0,'CodeSonar Alert':1,'Clang Rule':'N/A','CodeSonar Rule':rule,'Line':line,'True Positive':positive},ignore_index=True)
    elif line not in indexmap[alertpath]:
        indexmap[alertpath].update({line:index})
        if tool=='Clang':
            data=data.append({'Severity':severity,'CWE':cwe,'Clang Alert':1,'CodeSonar Alert':0,'Clang Rule':rule,'CodeSonar Rule':'N/A','Line':line,'True Positive':positive},ignore_index=True)
        elif tool=='gt-csonar':
            data=data.append({'Severity':'N/A','CWE':'N/A','Clang Alert':0,'CodeSonar Alert':1,'Clang Rule':'N/A','CodeSonar Rule':rule,'Line':line,'True Positive':positive},ignore_index=True)
    else:
        prev_entry=indexmap[alertpath][line]
        if tool=='Clang':
            data.set_value(prev_entry,'Clang Rule',rule)
            data.set_value(prev_entry,'Clang Alert',1)
            data.set_value(prev_entry,'CWE',cwe)
            data.set_value(prev_entry,'Severity',severity)
        elif tool=='gt-csonar':
            data.set_value(prev_entry,'CodeSonar Rule',rule)
            data.set_value(prev_entry,'CodeSonar Alert',1)
writer=ExcelWriter('combined_data_table.xlsx')
data.to_excel(writer,'sheet 1',index=False)
writer.save()
