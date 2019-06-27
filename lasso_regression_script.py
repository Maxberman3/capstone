import pandas as pd
import numpy as np
from pandas import ExcelWriter,ExcelFile
from sklearn.linear_model import LogisticRegressionCV

df=pd.read_excel('Juliet_Test_Suite/combined_data_table.xlsx')
# msk= np.random.rand(len(df))<0.8
# train=df[msk]
# test=df[~msk]
# train['Clang Rule']=train['Clang Rule'].astype('category').cat.codes
# train['CodeSonar Rule']=train['CodeSonar Rule'].astype('category').cat.codes
# train['Severity']=train['Severity'].astype('category').cat.codes
# train['CWE']=train['CWE'].astype('category').cat.codes
# test['Clang Rule']=test['Clang Rule'].astype('category').cat.codes
# test['CodeSonar Rule']=test['CodeSonar Rule'].astype('category').cat.codes
# test['Severity']=test['Severity'].astype('category').cat.codes
# test['CWE']=test['CWE'].astype('category').cat.codes
# X=train.iloc[:,:-1]
# y=train.iloc[:,-1]
df['Clang Rule']=df['Clang Rule'].astype('category').cat.codes
df['CodeSonar Rule']=df['CodeSonar Rule'].astype('category').cat.codes
df['Severity']=df['Severity'].astype('category').cat.codes
df['CWE']=df['CWE'].astype('category').cat.codes
df = df[np.isfinite(df['True Positive'])]
X=df.iloc[:,:-1]
y=df.iloc[:,-1]
clf=LogisticRegressionCV(cv=5,penalty='l1',solver='liblinear',scoring='accuracy').fit(X,y)
print(clf.score(X,y))
