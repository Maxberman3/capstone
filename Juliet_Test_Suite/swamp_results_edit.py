import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

results=pd.read_excel('Juliet_Test_Suite/SWAMP Results_ Clang & CodeSonar - Juliet Test Suite v1.3 for C_C++.xls')
for index,row in results.iterrows():
    path=row['Path']
    file=path.split('/')[-1]
    results.set_value(index,'Path',file)

writer=ExcelWriter('swampresults_edit.xlsx')
results.to_excel(writer,'sheet 1',index=False)
writer.save()
