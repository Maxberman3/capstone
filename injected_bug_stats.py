import pandas as pd
from pandas import ExcelFile

truthdf=pd.read_excel('bugs_table.xlsx')
bugids=set()
cwetypes={}

for index,row in truthdf.iterrows():
    bugids.add(row['Bug ID'])
    cwe1=row['CWE# 1']
    cwe2=row['CWE# 2']
    cwe3=row['CWE #3']
    if cwe1 not in cwetypes:
        cwetypes[cwe1]=1
    else:
        cwetypes[cwe1]+=1
    if cwe2 not in cwetypes:
        cwetypes[cwe2]=1
    else:
        cwetypes[cwe2]+=1
    if cwe3 not in cwetypes:
        cwetypes[cwe3]=1
    else:
        cwetypes[cwe3]+=1
print('The number of unique bug id\'s is '+str(len(bugids)))
print('The total number of alerts generated from injected bugs is '+str(index+1))
print('The number of alerts associated with each CWE type is:')
for key,value in cwetypes.items():
    print(str(key)+":"+str(value))
