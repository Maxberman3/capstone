import pandas as pd
from pandas import ExcelWriter,ExcelFile

bugsdf=pd.read_excel('Juliet_Test_Suite/swampresults_edit.xlsx')
truthdf=pd.read_excel('Juliet_Test_Suite/manifest.xlsx')
bugsdf['True Positive Flag']=0
bugsdf['File Match Flag']=0
bugsdf['CWE Match Flag']=0
truthdf['matched']=0
for index,row in bugsdf.iterrows():
    print(index)
    filepath=row['Path']
    line=row['Line']
    cwe=row['CWE']
    for indx2,truthrow in truthdf.iterrows():
        if truthrow['matched']==1:
            continue
        if filepath==truthrow['path']:
            bugsdf.set_value(index,'File Match Flag',1)
            if line==truthrow['line']:
                if cwe==truthrow['flaw name'].split(':')[0]:
                    bugsdf.set_value(index,'CWE Match Flag',1)
                bugsdf.set_value(index,'True Positive Flag',1)
                truthdf.set_value(indx2,'matched',1)
                break
writer=ExcelWriter('swampresults_edit_checked.xlsx')
bugsdf.to_excel(writer,'sheet 1',index=False)
writer.save()
