import pandas as pd
from pandas import ExcelWriter,ExcelFile

bugsdf=pd.read_excel('sql_cpp_bugs.xlsx')
truthdf=pd.read_excel('bugs_table_sql.xlsx')
bugsdf['True Positive Flag']=0
bugsdf['File Match Flag']=0
for index,row in bugsdf.iterrows():
    print(index)
    filepath=row['SourceFile']
    line=row['StartLine']
    for indx2,truthrow in truthdf.iterrows():
        if filepath==truthrow['File']:
            bugsdf.set_value(index,'File Match Flag',1)
            if line==truthrow['line']:
                bugsdf.set_value(index,'True Positive Flag',1)
                break
writer=ExcelWriter('cppbugs-checked-sql.xlsx')
bugsdf.to_excel(writer,'sheet 1',index=False)
writer.save()
