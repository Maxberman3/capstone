import pandas as pd
from pandas import ExcelFile

truthdf=pd.read_excel('bugs_table.xlsx')
bugids=set()
cwetypes={}

for index,row in truthdf.iterrows():
    bugids.add(row['Bug ID'])
    cert1=row['CERT#1']
    cert2=row['CERT#2']
    cert3=row['CERT#3']
    cert4=row['CERT #4']
    if cert1 not in cwetypes:
        cwetypes[cert1]=1
    else:
        cwetypes[cert1]+=1
    if cert2 not in cwetypes:
        cwetypes[cert2]=1
    else:
        cwetypes[cert2]+=1
    if cert3 not in cwetypes:
        cwetypes[cert3]=1
    else:
        cwetypes[cert3]+=1
    if cert4 not in cwetypes:
        cwetypes[cert4]=1
    else:
        cwetypes[cert4]+=1
print('The number of unique bug id\'s is '+str(len(bugids)))
print('The total number of alerts generated from injected bugs is '+str(index+1))
print('The number of alerts associated with each CWE type is:')
for key,value in cwetypes.items():
    print(str(key)+":"+str(value))
