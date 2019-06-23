import pandas as pd
from pandas import ExcelWriter,ExcelFile
import numpy as np

bugsdf=pd.read_excel('Juliet_Test_Suite/swampresults_edit.xlsx')
truthdf=pd.read_excel('Juliet_Test_Suite/manifest.xlsx')
bugsdf['True Positive Flag']=0
bugsdf['File Match Flag']=0
bugsdf['CWE Match Flag']=0
indexmap={}
for index,row in truthdf.iterrows():
    indexmap[row['path']]=index+2
# twentycount=0
for index,row in bugsdf.iterrows():
    print(index)
    # if(twentycount>499):
    #     break
    path=row['Path']
    if path in indexmap:
        bugsdf.set_value(index,'File Match Flag',1)
        truthindex=indexmap[path]
        line=row['Line']
        if str(row['CWE'])!='nan':
            cwe='CWE-'+str(int(row['CWE']))
        if truthdf.iloc[truthindex,2]==line:
            bugsdf.set_value(index,'True Positive Flag',1)
            if type(truthdf.iloc[truthindex,1]) is str:
                # print(cwe)
                # print(truthdf.iloc[truthindex,1].split(':')[0])
                # twentycount+=1
                if cwe==truthdf.iloc[truthindex,1].split(':')[0]:
                    # print('works')
                    bugsdf.set_value(index,'CWE Match Flag',1)
writer=ExcelWriter('swampresults_edit_checked.xlsx')
bugsdf.to_excel(writer,'sheet 1',index=False)
writer.save()
