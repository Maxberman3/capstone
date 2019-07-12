import pandas as pd
import numpy as np
from pandas import ExcelWriter,ExcelFile
from sklearn.linear_model import LogisticRegressionCV

def encode_and_bind(original_dataframe, feature_to_encode):
    res = pd.concat([original_dataframe, pd.get_dummies(original_dataframe[feature_to_encode],prefix=feature_to_encode,dummy_na=True)], axis=1)
    res.drop(columns=[feature_to_encode],axis=1,inplace=True)
    return(res)

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
df=encode_and_bind(df,'Clang Rule')
df=encode_and_bind(df,'CodeSonar Rule')
df=encode_and_bind(df,'Severity')
df=encode_and_bind(df,'CWE')
df = df[np.isfinite(df['True Positive'])]
df = df[np.isfinite(df['True Positive'])]
X=df.iloc[:,:-1]
y=df.iloc[:,-1]
clf=LogisticRegressionCV(cv=5,penalty='l1',solver='liblinear',scoring='accuracy').fit(X,y)
print(clf.score(X,y))
